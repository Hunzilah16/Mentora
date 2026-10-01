"""
Expanded High-Precision Biological Diagram Generator for Cambridge AS Biology (9700)
Generates 12 publication-quality biological figures for Topic 1: Cell Structure
Output directory: z:\\tests n quizes63\\books\\psycology\\new styl\\AS biology cambrege\\diagrams
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

NAVY = "#0b1b36"
CRIMSON = "#a81717"
DARK_GREY = "#20242e"
MID_GREY = "#5a6275"
LIGHT_GREY = "#e8eaed"
CYTOPLASM_BG = "#f6f8fb"
NUCLEUS_BG = "#e5ecf6"
MITO_COLOR = "#fce8e6"
CHLORO_COLOR = "#e6f4ea"

def generate_animal_cell_tem(filename="fig1_1_animal_cell_tem.png"):
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.axis('off')
    cell = FancyBboxPatch((18, 8), 64, 52, boxstyle="round,pad=3,rounding_size=15",
                          facecolor=CYTOPLASM_BG, edgecolor=NAVY, linewidth=2)
    ax.add_patch(cell)
    # Microvilli
    mv_path = [(65, 60), (66, 66), (67, 60), (69, 67), (70, 60), (72, 66), (73, 60), (75, 65), (76, 59)]
    mv_codes = [Path.MOVETO] + [Path.LINETO]*(len(mv_path)-1)
    ax.add_patch(PathPatch(Path(mv_path, mv_codes), facecolor=CYTOPLASM_BG, edgecolor=NAVY, linewidth=1.5))
    # Nucleus & Nucleolus
    ax.add_patch(Circle((42, 35), 14, facecolor=NUCLEUS_BG, edgecolor=NAVY, linewidth=1.8, linestyle='--'))
    ax.add_patch(Circle((42, 35), 13.2, facecolor=NUCLEUS_BG, edgecolor=NAVY, linewidth=1.0))
    ax.add_patch(Circle((45, 37), 4.2, facecolor="#8fa3c7", edgecolor=NAVY, linewidth=1.2))
    # RER
    for offset in [16, 18.5, 21]:
        ax.add_patch(patches.Arc((42, 35), offset*2, offset*1.6, angle=0, theta1=60, theta2=190, color=NAVY, linewidth=1.3))
        for a in np.linspace(65, 185, 10):
            rad = np.radians(a)
            ax.plot(42 + (offset+0.4)*np.cos(rad), 35 + (offset*0.8+0.3)*np.sin(rad), 'o', color=DARK_GREY, markersize=1.8)
    # Mitochondria
    def draw_mito(mx, my, angle):
        ax.add_patch(Ellipse((mx, my), 12, 6, angle=angle, facecolor=MITO_COLOR, edgecolor=CRIMSON, linewidth=1.4))
        rad = np.radians(angle)
        cos_a, sin_a = np.cos(rad), np.sin(rad)
        for x1, y1, x2, y2 in [(-4, -1.8, -4, 1.8), (-1.5, -2.2, -1.5, 1.5), (1.5, -2.0, 1.5, 2.0), (4, -1.5, 4, 1.5)]:
            ax.plot([mx + x1*cos_a - y1*sin_a, mx + x2*cos_a - y2*sin_a],
                    [my + x1*sin_a + y1*cos_a, my + x2*sin_a + y2*cos_a], color=CRIMSON, linewidth=1.0)
    draw_mito(66, 24, 25)
    draw_mito(24, 20, -35)
    # Golgi
    for gy in [42, 44.5, 47, 49.5]:
        gx = np.linspace(62, 73, 30)
        ax.plot(gx, gy + 1.2 * np.sin(np.pi * (gx - 62)/11), color=NAVY, linewidth=1.4)
    for vx, vy in [(60, 43), (74, 46), (76, 51), (71, 54), (63, 40)]:
        ax.add_patch(Circle((vx, vy), 1.0, facecolor="#fdecc8", edgecolor=NAVY, linewidth=1.0))
    # Centrosome
    ax.add_patch(Rectangle((28, 44), 1.5, 4.5, angle=15, facecolor="#555", edgecolor=NAVY, linewidth=1))
    ax.add_patch(Rectangle((30, 43), 4.5, 1.5, angle=15, facecolor="#555", edgecolor=NAVY, linewidth=1))
    # Labels
    for label, px, py, tx, ty in [
        ("A (Nuclear envelope with pores)", 42, 49, 32, 63),
        ("B (Nucleolus)", 45, 37, 48, 63),
        ("C (Rough endoplasmic reticulum)", 30, 48, 12, 58),
        ("D (Centrioles)", 29, 45, 10, 44),
        ("E (Lysosome)", 28, 30, 10, 30),
        ("F (Mitochondrion)", 66, 24, 82, 24),
        ("G (Golgi apparatus)", 68, 47, 84, 45),
        ("H (Microvilli)", 71, 63, 85, 63),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))
    ax.plot([22, 38], [11, 11], color=DARK_GREY, linewidth=3)
    ax.text(30, 12.5, r"$5\ \mu\mathrm{m}$", ha="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)
    ax.text(50, 2, "Fig. 1.1: Transmission electron micrograph (TEM) diagram of an animal cell",
            ha="center", fontsize=8.2, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_plant_cell_tem(filename="fig1_2_plant_cell_tem.png"):
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 70); ax.axis('off')
    ax.add_patch(FancyBboxPatch((15, 8), 70, 52, boxstyle="round,pad=2,rounding_size=6",
                               facecolor="#e8f5e9", edgecolor="#2e7d32", linewidth=3.5))
    ax.add_patch(FancyBboxPatch((16.5, 9.5), 67, 49, boxstyle="round,pad=1.5,rounding_size=5",
                               facecolor=CYTOPLASM_BG, edgecolor="#1b5e20", linewidth=1.5))
    vacuole = FancyBboxPatch((32, 16), 46, 36, boxstyle="round,pad=2,rounding_size=10",
                             facecolor="#e1f5fe", edgecolor="#0288d1", linewidth=1.8)
    ax.add_patch(vacuole)
    ax.text(55, 34, "Cell Sap /\nCentral Vacuole", ha="center", va="center", fontsize=7.5, color="#0277bd", style="italic")
    ax.add_patch(Circle((24, 45), 6.5, facecolor=NUCLEUS_BG, edgecolor=NAVY, linewidth=1.5))
    ax.add_patch(Circle((24, 45), 2.2, facecolor="#8fa3c7", edgecolor=NAVY, linewidth=1.0))
    def draw_chloro(cx, cy, angle):
        ax.add_patch(Ellipse((cx, cy), 13, 6.5, angle=angle, facecolor=CHLORO_COLOR, edgecolor="#2e7d32", linewidth=1.5))
        rad = np.radians(angle)
        cos_a, sin_a = np.cos(rad), np.sin(rad)
        for gx in [-3, 0, 3]:
            for ty in [-1.5, -0.5, 0.5, 1.5]:
                rx, ry = cx + gx*cos_a - ty*sin_a, cy + gx*sin_a + ty*cos_a
                ax.plot([rx-1*cos_a, rx+1*cos_a], [ry-1*sin_a, ry+1*sin_a], color="#1b5e20", linewidth=1.2)
    draw_chloro(25, 20, 30)
    draw_chloro(55, 54, 0)
    for py in [20, 35, 50]:
        ax.plot([14.5, 17], [py, py], color="white", linewidth=2.5)
    for label, px, py, tx, ty in [
        ("A (Cellulose cell wall)", 15, 45, 3, 58),
        ("B (Tonoplast / vacuole membrane)", 40, 50, 30, 63),
        ("C (Chloroplast with grana)", 55, 57, 72, 63),
        ("D (Nucleus & nucleolus)", 24, 51, 8, 50),
        ("E (Mitochondrion)", 22, 33, 5, 33),
        ("F (Plasmodesma)", 15, 20, 4, 18),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))
    ax.plot([50, 72], [11, 11], color=DARK_GREY, linewidth=3)
    ax.text(61, 12.5, r"$10\ \mu\mathrm{m}$", ha="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)
    ax.text(50, 2, "Fig. 1.2: Fine structure of a photosynthetic plant mesophyll cell",
            ha="center", fontsize=8.2, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_prokaryote_bacterium(filename="fig1_3_bacterium_prokaryote.png"):
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 65); ax.axis('off')
    ax.add_patch(FancyBboxPatch((25, 18), 50, 28, boxstyle="round,pad=3,rounding_size=14", facecolor="#fff3e0", edgecolor="#e65100", linewidth=1.5, linestyle=":"))
    ax.add_patch(FancyBboxPatch((26.5, 19.5), 47, 25, boxstyle="round,pad=2,rounding_size=12", facecolor="#ffe0b2", edgecolor="#bf360c", linewidth=2.0))
    ax.add_patch(FancyBboxPatch((28, 21), 44, 22, boxstyle="round,pad=1.5,rounding_size=10", facecolor="#f9fbe7", edgecolor=NAVY, linewidth=1.2))
    t = np.linspace(0, 14*np.pi, 500)
    ax.plot(50 + 10*np.sin(t) + 3*np.sin(3*t), 32 + 5*np.cos(t) + 2*np.cos(4*t), color=CRIMSON, linewidth=1.2, alpha=0.85)
    for px, py in [(35, 27), (65, 36), (62, 25)]:
        ax.add_patch(Circle((px, py), 2.0, facecolor="none", edgecolor=CRIMSON, linewidth=1.4))
    np.random.seed(101)
    for _ in range(40):
        ax.plot(np.random.uniform(32, 68), np.random.uniform(24, 40), 'o', color=DARK_GREY, markersize=1.5)
    fx = np.linspace(22, 4, 100)
    ax.plot(fx, 32 + 6*np.sin(0.4*(fx - 22)), color="#bf360c", linewidth=2.2)
    for label, px, py, tx, ty in [
        ("A (Circular DNA / nucleoid)", 50, 34, 42, 56),
        ("B (Plasmid)", 65, 36, 76, 52),
        ("C (70S Ribosomes)", 40, 27, 25, 10),
        ("D (Peptidoglycan cell wall)", 27, 38, 12, 48),
        ("E (Capsule / slime layer)", 25, 42, 12, 56),
        ("F (Flagellum)", 10, 32, 2, 22),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))
    ax.plot([42, 58], [18, 18], color=DARK_GREY, linewidth=3)
    ax.text(50, 19.5, r"$1.0\ \mu\mathrm{m}$", ha="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)
    ax.text(50, 2, "Fig. 1.3: Generalized ultrastructure of a prokaryotic cell (bacterium)", ha="center", fontsize=8.2, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_graticule_micrometer(filename="fig1_4_graticule_micrometer.png"):
    fig, ax = plt.subplots(figsize=(7.5, 4.2), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 55); ax.axis('off')
    ax.text(10, 48, "Eyepiece Graticule (arbitrary units):", fontsize=8.0, fontweight="bold", color=NAVY)
    ax.plot([15, 85], [42, 42], color=NAVY, linewidth=1.5)
    for i in range(51):
        x = 15 + i * (70 / 50)
        if i % 10 == 0:
            ax.plot([x, x], [42, 46], color=NAVY, linewidth=1.2)
            ax.text(x, 47, str(i * 2), ha="center", fontsize=7.0, fontweight="bold", color=NAVY)
        elif i % 5 == 0:
            ax.plot([x, x], [42, 44.5], color=NAVY, linewidth=1.0)
        else:
            ax.plot([x, x], [42, 43.5], color=NAVY, linewidth=0.6)
    ax.text(10, 25, r"Stage Micrometer ($1\ \mathrm{small\ division} = 10\ \mu\mathrm{m} = 0.01\ \mathrm{mm}$):",
            fontsize=8.0, fontweight="bold", color=CRIMSON)
    ax.plot([15, 85], [18, 18], color=CRIMSON, linewidth=1.5)
    for i in range(21):
        x = 15 + i * (28.0 / 10.0)
        if i % 10 == 0:
            ax.plot([x, x], [14, 18], color=CRIMSON, linewidth=1.4)
            ax.text(x, 11, f"{i*0.01:.2f} mm", ha="center", fontsize=7.0, fontweight="bold", color=CRIMSON)
        elif i % 5 == 0:
            ax.plot([x, x], [15.5, 18], color=CRIMSON, linewidth=1.0)
        else:
            ax.plot([x, x], [16.5, 18], color=CRIMSON, linewidth=0.6)
    ax.plot([15, 15], [18, 42], color="#888", linestyle="--", linewidth=1.0)
    ax.plot([71, 71], [18, 42], color="#888", linestyle="--", linewidth=1.0)
    ax.annotate("40 graticule units =\n0.20 mm (200 um)", xy=(71, 30), xytext=(76, 28),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=0.8),
                fontsize=7.0, fontweight="bold", color=CRIMSON)
    ax.text(50, 3, "Fig. 1.4: Calibration of an eyepiece graticule against a stage micrometer scale under ×400 total magnification",
            ha="center", fontsize=8.0, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_virus_hiv(filename="fig1_5_virus_structure.png"):
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 65); ax.axis('off')
    ax.add_patch(Circle((50, 32), 18, facecolor="#e8eaf6", edgecolor="#3f51b5", linewidth=2.0))
    for a in np.linspace(0, 2*np.pi, 20, endpoint=False):
        sx, sy = 50 + 18*np.cos(a), 32 + 18*np.sin(a)
        ex, ey = 50 + 22.5*np.cos(a), 32 + 22.5*np.sin(a)
        ax.plot([sx, ex], [sy, ey], color=CRIMSON, linewidth=1.5)
        ax.plot(ex, ey, 'o', color=CRIMSON, markersize=3.5)
    ax.add_patch(Polygon([(44, 21), (56, 21), (54, 42), (46, 42)], facecolor="#c5cae9", edgecolor=NAVY, linewidth=1.5))
    t = np.linspace(24, 38, 80)
    ax.plot(48 + 1.2*np.sin(1.2*(t-24)), t, color="#d32f2f", linewidth=1.5)
    ax.plot(52 + 1.2*np.sin(1.2*(t-24)), t, color="#d32f2f", linewidth=1.5)
    ax.plot(48, 28, 's', color=NAVY, markersize=4)
    ax.plot(52, 34, 's', color=NAVY, markersize=4)
    for label, px, py, tx, ty in [
        ("A (Glycoprotein gp120 spike)", 66, 48, 76, 56),
        ("B (Phospholipid bilayer envelope)", 63, 44, 76, 44),
        ("C (Protein capsid shell / p24)", 55, 30, 76, 30),
        ("D (Single-stranded viral RNA)", 49, 36, 18, 48),
        ("E (Reverse transcriptase enzyme)", 48, 28, 18, 32),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))
    ax.plot([38, 62], [7, 7], color=DARK_GREY, linewidth=3)
    ax.text(50, 8.5, r"$100\ \mathrm{nm}\ (0.1\ \mu\mathrm{m})$", ha="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)
    ax.text(50, 1.5, "Fig. 1.5: Diagrammatic representation of human immunodeficiency virus (HIV)",
            ha="center", fontsize=8.2, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_chloroplast_tem(filename="fig1_7_chloroplast_tem.png"):
    """Fig 1.7: Detailed Chloroplast Fine Structure (TEM schematic)"""
    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
    
    # Double membrane envelope
    ax.add_patch(Ellipse((50, 30), 80, 46, facecolor=CHLORO_COLOR, edgecolor="#1b5e20", linewidth=2.0))
    ax.add_patch(Ellipse((50, 30), 77, 43, facecolor=CHLORO_COLOR, edgecolor="#2e7d32", linewidth=1.0))
    
    # Grana stacks (thylakoid discs)
    grana_x = [28, 42, 58, 72]
    for gx in grana_x:
        for gy in np.linspace(20, 38, 7):
            ax.add_patch(FancyBboxPatch((gx-4, gy-0.8), 8, 1.6, boxstyle="round,pad=0.1",
                                       facecolor="#1b5e20", edgecolor="#0d3810", linewidth=0.8))
    
    # Intergranal lamellae (connecting thylakoids)
    for y_conn in [23, 29, 35]:
        ax.plot([24, 76], [y_conn, y_conn], color="#2e7d32", linewidth=1.2)
        
    # Starch grain & lipid droplet
    ax.add_patch(Ellipse((35, 17), 10, 5, angle=20, facecolor="#fff9c4", edgecolor="#fbc02d", linewidth=1.2))
    ax.text(35, 17, "Starch", ha="center", va="center", fontsize=6.5, color="#f57f17", fontweight="bold")
    ax.add_patch(Circle((65, 16), 2.5, facecolor="#ffe082", edgecolor="#ffb300", linewidth=1.0))
    
    # Circular DNA loop & 70S ribosomes
    t = np.linspace(0, 2*np.pi, 50)
    ax.plot(52 + 3*np.cos(t), 16 + 2*np.sin(t), color=CRIMSON, linewidth=1.2)
    for rx, ry in [(45, 42), (48, 44), (55, 43), (62, 41), (32, 40)]:
        ax.plot(rx, ry, 'o', color=DARK_GREY, markersize=1.8)

    # Labels
    for label, px, py, tx, ty in [
        ("A (Outer membrane)", 18, 38, 6, 50),
        ("B (Thylakoid stack / Granum)", 42, 38, 30, 53),
        ("C (Intergranal lamella)", 50, 29, 50, 48),
        ("D (Stroma / site of Calvin cycle)", 68, 35, 78, 50),
        ("E (Circular chloroplast DNA)", 52, 16, 52, 6),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))
                    
    # Scale bar (2 um)
    ax.plot([72, 86], [10, 10], color=DARK_GREY, linewidth=3)
    ax.text(79, 11.5, r"$2.0\ \mu\mathrm{m}$", ha="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)
    ax.text(50, 1.5, "Fig. 1.7: Transmission electron micrograph schematic of a chloroplast",
            ha="center", fontsize=8.0, fontweight="bold", color=NAVY, style="italic")
            
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_nucleus_tem(filename="fig1_8_nucleus_tem.png"):
    """Fig 1.8: High-Resolution Nucleus & Nuclear Pore Complex"""
    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
    
    # Outer & inner nuclear envelope
    ax.add_patch(Ellipse((45, 30), 65, 44, facecolor=NUCLEUS_BG, edgecolor=NAVY, linewidth=2.0))
    ax.add_patch(Ellipse((45, 30), 62, 41, facecolor=NUCLEUS_BG, edgecolor=NAVY, linewidth=1.2))
    
    # Nuclear pores (breaks in the envelope)
    for angle in [30, 65, 115, 150, 210, 250, 310, 345]:
        rad = np.radians(angle)
        x = 45 + 31.7 * np.cos(rad)
        y = 30 + 21.2 * np.sin(rad)
        ax.plot([x-1.5*np.cos(rad), x+1.5*np.cos(rad)], [y-1.5*np.sin(rad), y+1.5*np.sin(rad)], color="white", linewidth=4.0)
        ax.plot(x, y, 'o', color=CRIMSON, markersize=3.0)
        
    # Nucleolus
    ax.add_patch(Circle((52, 33), 8.5, facecolor="#8fa3c7", edgecolor=NAVY, linewidth=1.5))
    ax.text(52, 33, "Dense\nNucleolus", ha="center", va="center", fontsize=7.0, color="white", fontweight="bold")
    
    # Chromatin network
    np.random.seed(99)
    for _ in range(25):
        cx = 45 + np.random.uniform(-22, 22)
        cy = 30 + np.random.uniform(-14, 14)
        if (cx-52)**2 + (cy-33)**2 > 70:
            ax.add_patch(Ellipse((cx, cy), 3, 1.5, angle=np.random.uniform(0, 180), facecolor="#5d7294", alpha=0.7))
            
    # Attached RER cisternae with ribosomes
    arc = patches.Arc((45, 30), 75, 52, angle=0, theta1=20, theta2=100, color=NAVY, linewidth=1.5)
    ax.add_patch(arc)
    for a in np.linspace(25, 95, 8):
        rad = np.radians(a)
        ax.plot(45 + 38*np.cos(rad), 30 + 26.5*np.sin(rad), 'o', color=DARK_GREY, markersize=2.0)

    # Labels
    for label, px, py, tx, ty in [
        ("A (Nuclear pore complex)", 65, 45, 78, 52),
        ("B (Double nuclear envelope)", 25, 45, 8, 52),
        ("C (Perinuclear space)", 18, 30, 4, 30),
        ("D (Nucleolus / ribosome biogenesis)", 52, 33, 76, 33),
        ("E (Heterochromatin)", 32, 22, 12, 14),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))

    ax.plot([45, 65], [8, 8], color=DARK_GREY, linewidth=3)
    ax.text(55, 9.5, r"$2.0\ \mu\mathrm{m}$", ha="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)
    ax.text(50, 1.5, "Fig. 1.8: Transmission electron micrograph diagram of the eukaryotic nucleus",
            ha="center", fontsize=8.0, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_golgi_secretory(filename="fig1_9_golgi_secretory.png"):
    """Fig 1.9: Golgi Apparatus Secretory Pathway"""
    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')

    # Cisternae curved from cis face (bottom) to trans face (top)
    colors = ["#c5cae9", "#9fa8da", "#7986cb", "#5c6bc0"]
    for i, cy in enumerate([18, 23, 28, 33]):
        gx = np.linspace(30, 70, 50)
        curve = cy + 3.0 * np.sin(np.pi * (gx - 30)/40)
        ax.plot(gx, curve, color=NAVY, linewidth=2.5)
        ax.plot(gx, curve-0.8, color=colors[i], linewidth=2.0)

    # Incoming transport vesicles from RER (cis face)
    for vx, vy in [(36, 12), (50, 11), (64, 12)]:
        ax.add_patch(Circle((vx, vy), 2.2, facecolor="#ffe0b2", edgecolor=NAVY, linewidth=1.2))
        ax.annotate("", xy=(vx, vy+4), xytext=(vx, vy+1), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0))

    # Outgoing secretory vesicles from trans face
    for vx, vy in [(34, 42), (48, 44), (62, 42), (55, 50)]:
        ax.add_patch(Circle((vx, vy), 2.5, facecolor="#ffcc80", edgecolor=CRIMSON, linewidth=1.4))

    # Cell surface membrane and exocytosis at top
    ax.plot([20, 80], [55, 55], color=NAVY, linewidth=2.5)
    # Exocytosing vesicle fusion
    arc = patches.Arc((50, 55), 8, 8, angle=0, theta1=180, theta2=360, color=CRIMSON, linewidth=2.0)
    ax.add_patch(arc)
    ax.plot([46, 54], [55, 55], color="white", linewidth=3.0)

    # Labels
    for label, px, py, tx, ty in [
        ("A (cis face / receiving cisternae)", 32, 19, 6, 19),
        ("B (trans face / shipping cisternae)", 32, 35, 6, 35),
        ("C (Incoming transport vesicle from RER)", 50, 11, 74, 11),
        ("D (Secretory vesicle)", 62, 42, 78, 42),
        ("E (Exocytosis at cell surface membrane)", 50, 55, 68, 55),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))

    ax.text(50, 2, "Fig. 1.9: Diagram of Golgi apparatus polarity and vesicular transport to plasma membrane",
            ha="center", fontsize=8.0, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_centriole_microtubule(filename="fig1_10_centriole_structure.png"):
    """Fig 1.10: Centriole 9+0 Triplet Microtubule Ring Structure"""
    fig, ax = plt.subplots(figsize=(7.0, 4.5), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')
    
    center = (50, 30)
    radius = 16
    angles = np.linspace(0, 2*np.pi, 9, endpoint=False)
    
    for i, a in enumerate(angles):
        # 3 microtubules in each triplet (A, B, C tubules)
        for t_idx, t_offset in enumerate([-1.6, 0, 1.6]):
            rad = a + np.radians(15 * t_offset)
            r = radius + t_offset * 1.8
            tx = center[0] + r * np.cos(rad)
            ty = center[1] + r * np.sin(rad)
            ax.add_patch(Circle((tx, ty), 1.4, facecolor="#90caf9", edgecolor=NAVY, linewidth=1.2))

    # Inner cartwheel hub and spokes (9+0 arrangement)
    ax.add_patch(Circle(center, 2.5, facecolor="#37474f", edgecolor=NAVY, linewidth=1.2))
    for a in angles:
        sx = center[0] + 2.5 * np.cos(a)
        sy = center[1] + 2.5 * np.sin(a)
        ex = center[0] + (radius - 3) * np.cos(a)
        ey = center[1] + (radius - 3) * np.sin(a)
        ax.plot([sx, ex], [sy, ey], color="#78909c", linewidth=1.0)

    # Labels
    for label, px, py, tx, ty in [
        ("A (Triplet of microtubules: A, B, C tubules)", 66, 35, 74, 48),
        ("B (Central hub of cartwheel)", 50, 30, 18, 48),
        ("C (Radial spoke connecting hub to triplet)", 42, 24, 14, 20),
        ("D (9+0 arrangement: absence of central microtubules)", 50, 44, 15, 10),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))

    # Scale bar (200 nm)
    ax.plot([72, 88], [8, 8], color=DARK_GREY, linewidth=3)
    ax.text(80, 9.5, r"$200\ \mathrm{nm}$", ha="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)
    ax.text(50, 2, "Fig. 1.10: Transverse section schematic of a centriole showing 9+0 triplet microtubule architecture",
            ha="center", fontsize=8.0, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_microvilli_epithelium(filename="fig1_11_microvilli_epithelium.png"):
    """Fig 1.11: Intestinal Epithelial Cell Apical Microvilli with Actin Core"""
    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 60); ax.axis('off')

    # Brush border: row of microvilli
    mv_peaks = [20, 28, 36, 44, 52, 60, 68, 76]
    for px in mv_peaks:
        ax.add_patch(FancyBboxPatch((px-2.5, 25), 5.0, 24, boxstyle="round,pad=0.5,rounding_size=2.0",
                                   facecolor="#fff8e1", edgecolor="#f57f17", linewidth=1.5))
        # Actin core filaments
        for ax_off in [-1.0, 0, 1.0]:
            ax.plot([px+ax_off, px+ax_off], [18, 48], color="#e65100", linewidth=1.2)

    # Terminal web actin network below microvilli
    for y_net in [18, 20, 22]:
        ax.plot([14, 82], [y_net, y_net], color="#bf360c", linewidth=1.2, linestyle="--")

    # Tight junction between cells
    ax.plot([14, 14], [10, 26], color=NAVY, linewidth=3.0)
    ax.plot([82, 82], [10, 26], color=NAVY, linewidth=3.0)

    # Labels
    for label, px, py, tx, ty in [
        ("A (Apical plasma membrane of microvillus)", 44, 48, 14, 54),
        ("B (Core bundle of actin microfilaments)", 52, 35, 78, 42),
        ("C (Terminal web cytoskeletal anchor)", 60, 20, 78, 20),
        ("D (Tight junction preventing paracellular leak)", 14, 20, 4, 12),
    ]:
        ax.annotate(label, xy=(px, py), xytext=(tx, ty),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                    fontsize=7.5, fontweight="bold", color=NAVY,
                    bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=0.85))

    # Scale bar (1 um)
    ax.plot([72, 86], [8, 8], color=DARK_GREY, linewidth=3)
    ax.text(79, 9.5, r"$1.0\ \mu\mathrm{m}$", ha="center", fontsize=7.5, fontweight="bold", color=DARK_GREY)
    ax.text(50, 2, "Fig. 1.11: Fine structure of the intestinal brush border showing microvilli and cytoskeleton",
            ha="center", fontsize=8.0, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_resolution_diffraction(filename="fig1_12_resolution_diffraction.png"):
    """Fig 1.12: Rayleigh Criterion of Resolution (Airy Disks)"""
    fig, ax = plt.subplots(figsize=(7.5, 4.2), dpi=300)
    ax.set_xlim(0, 100); ax.set_ylim(0, 55); ax.axis('off')

    x = np.linspace(-15, 15, 200)
    # Sinc function for airy disk profile
    def airy(x_val):
        return (np.sin(np.pi*x_val + 1e-9) / (np.pi*x_val + 1e-9))**2

    # Case 1: Unresolved (too close)
    ax.text(25, 48, "Case 1: Unresolved\n(Points closer than limit d)", ha="center", fontsize=7.5, fontweight="bold", color=CRIMSON)
    y1 = airy(x/3) + airy((x-2)/3)
    ax.plot(x + 25, y1 * 25 + 10, color=CRIMSON, linewidth=1.8)

    # Case 2: Resolved (Rayleigh criterion)
    ax.text(75, 48, "Case 2: Fully Resolved\n(Separation >= limit d)", ha="center", fontsize=7.5, fontweight="bold", color=NAVY)
    y2_a = airy(x/3)
    y2_b = airy((x-6)/3)
    ax.plot(x + 75, (y2_a + y2_b) * 25 + 10, color=NAVY, linewidth=1.8)
    ax.plot(x + 75, y2_a * 25 + 10, color=NAVY, linewidth=0.8, linestyle=":")
    ax.plot(x + 75, y2_b * 25 + 10, color=NAVY, linewidth=0.8, linestyle=":")

    # Minimum dip between peaks
    ax.annotate("Distinct central dip\nallows resolution", xy=(78, 22), xytext=(78, 5),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.9),
                fontsize=7.0, fontweight="bold", color=NAVY, ha="center")

    ax.text(50, 1.5, "Fig. 1.12: Diffraction patterns and resolution limit (Rayleigh criterion) for light vs electron waves",
            ha="center", fontsize=8.0, fontweight="bold", color=NAVY, style="italic")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    return out_path

def generate_all_expanded():
    print("Generating complete expanded diagram suite (12 figures)...")
    generate_animal_cell_tem()
    generate_plant_cell_tem()
    generate_prokaryote_bacterium()
    generate_graticule_micrometer()
    generate_virus_hiv()
    generate_chloroplast_tem()
    generate_nucleus_tem()
    generate_golgi_secretory()
    generate_centriole_microtubule()
    generate_microvilli_epithelium()
    generate_resolution_diffraction()
    print("All 12 biological diagrams generated successfully.")

if __name__ == "__main__":
    generate_all_expanded()
