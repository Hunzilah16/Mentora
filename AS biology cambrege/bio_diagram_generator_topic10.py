"""
Vector Diagram Generator for Topic 10: Infectious Diseases
Cambridge International AS Level Biology (9700)
Candidate: Hamna | Mentora Academy

Generates 14 high-resolution 300 DPI scientific figures:
- fig10_1: Comparative taxonomy & transmission of the 4 major pathogens (Cholera, Malaria, TB, HIV)
- fig10_2: Ultrastructure of Vibrio cholerae (Gram-negative bacterium, single polar flagellum)
- fig10_3: Choleragen enterotoxin mechanism: cAMP cascade, CFTR opening, Cl- & water secretion
- fig10_4: Physiology of Oral Rehydration Therapy (ORT): SGLT1 glucose-Na+ cotransport
- fig10_5: Complete life cycle of Plasmodium (hepatic schizogony, erythrocytic cycle, mosquito gut)
- fig10_6: Erythrocytic schizogony and cyclical fever paroxysms of Plasmodium falciparum
- fig10_7: Histopathology of Tuberculosis: alveolar macrophage infection, tubercle formation, cavitation
- fig10_8: Ultrastructure of HIV retrovirus (gp120/gp41, envelope, capsid, reverse transcriptase, ssRNA)
- fig10_9: Replication cycle of HIV in CD4+ T-helper lymphocyte (entry, reverse transcription, integration)
- fig10_10: Clinical stages of HIV: CD4 count vs viral load progression to AIDS
- fig10_11: Penicillin mode of action: transpeptidase inhibition, defective peptidoglycan, osmotic lysis
- fig10_12: Molecular mechanisms of antibiotic resistance (beta-lactamase, efflux pumps, mutated targets)
- fig10_13: Horizontal vs vertical gene transmission: R-plasmid conjugation vs binary fission
- fig10_14: Selection pressure dynamics: evolution of antibiotic resistance in bacterial populations
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
# Fig 10.1: Comparative Taxonomy of 4 Major Pathogens
# -----------------------------------------------------------------------------
def generate_fig10_1():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 10.1: Comparative Taxonomy and Transmission of Four Major Infectious Diseases")
    ax.axis("off")

    columns = ["Disease", "Pathogen & Classification", "Transmission Route", "Site of Infection", "Global Prevention"]
    rows = [
        ["Cholera", "Vibrio cholerae\n(Gram-negative bacterium)", "Water-borne & food-borne\n(Faecal-oral route)", "Small intestine\n(enterocyte epithelium)", "Piped treated water,\nsewage sanitation, ORT"],
        ["Malaria", "Plasmodium spp. (falciparum)\n(Unicellular protoctist)", "Vector-borne: female\nAnopheles mosquito bite", "Liver hepatocytes &\nerythrocytes (RBCs)", "ITNs, indoor spraying,\nACT drugs, RTS,S vaccine"],
        ["Tuberculosis", "Mycobacterium tuberculosis\n(Acid-fast bacterium)", "Airborne aerosol droplets\n(Coughing, sneezing)", "Lungs (alveoli) &\nsecondary organs", "BCG vaccination, DOTS\n(6-9 mo multi-antibiotics)"],
        ["HIV / AIDS", "Human Immunodeficiency Virus\n(Enveloped ssRNA retrovirus)", "Sexual contact, blood,\nneedles, mother-to-child", "T-helper lymphocytes\n(CD4+ cells) & macrophages", "Barrier contraceptives,\nsafe blood, needle ex., ART"]
    ]

    cell_colors = [
        ["#dbeafe", "#eff6ff", "#eff6ff", "#eff6ff", "#f0fdf4"],
        ["#fee2e2", "#fef2f2", "#fef2f2", "#fef2f2", "#f0fdf4"],
        ["#fef3c7", "#fffbeb", "#fffbeb", "#fffbeb", "#f0fdf4"],
        ["#f3e8ff", "#faf5ff", "#faf5ff", "#faf5ff", "#f0fdf4"]
    ]

    table = ax.table(cellText=rows, colLabels=columns, cellColours=cell_colors,
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(7.2)
    table.scale(1.0, 2.3)

    for col in range(len(columns)):
        cell = table[0, col]
        cell.set_facecolor(NAVY)
        cell.set_text_props(color="white", fontweight="bold", fontsize=8)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_1.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.2: Ultrastructure of Vibrio cholerae
# -----------------------------------------------------------------------------
def generate_fig10_2():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 10.2: Ultrastructure and Anatomy of Vibrio cholerae")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Vibrio comma-shaped body (curved rod)
    verts = [
        (3.0, 6.5), (5.5, 7.2), (7.0, 6.0), (7.2, 4.5), (6.0, 3.2),
        (4.2, 3.0), (3.0, 4.0), (2.8, 5.5), (3.0, 6.5)
    ]
    path = Path(verts, [Path.MOVETO] + [Path.CURVE4]*7 + [Path.CLOSEPOLY])
    patch = patches.PathPatch(path, facecolor="#eff6ff", edgecolor=NAVY, lw=2.0)
    ax.add_patch(patch)

    # Flagellum (single polar flagellum, sheathed)
    t = np.linspace(0, 4*np.pi, 100)
    fx = 7.1 + 0.3 * t
    fy = 4.5 + 0.5 * np.sin(t)
    ax.plot(fx, fy, color=STEEL_BLUE, lw=2.5)
    ax.text(8.8, 5.8, "Single Polar\nFlagellum\n(Motility across\nmucus blanket)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)

    # Internal details:
    # Peptidoglycan cell wall & outer membrane (Gram -ve)
    ax.text(4.8, 6.4, "Outer Membrane (LPS) &\nThin Peptidoglycan Wall (Gram -ve)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)

    # Circular Chromosome (Nucleoid)
    t_n = np.linspace(0, 2*np.pi, 50)
    nx = 4.2 + 0.8 * np.cos(t_n) + 0.2 * np.sin(3*t_n)
    ny = 4.6 + 0.6 * np.sin(t_n) + 0.1 * np.cos(2*t_n)
    ax.plot(nx, ny, color=CRIMSON, lw=2.0)
    ax.text(4.2, 4.6, "Circular DNA\n(Nucleoid)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # 70S Ribosomes
    for rx, ry in [(3.4, 5.4), (3.8, 3.8), (5.6, 5.2), (6.2, 4.2), (5.2, 3.8), (3.6, 4.4)]:
        ax.plot(rx, ry, "o", color=STEEL_BLUE, markersize=3.5)
    ax.text(3.4, 3.3, "70S Ribosomes", ha="center", va="center", fontsize=7, color=STEEL_BLUE)

    # Toxin-coregulated pilus (TCP)
    for px, py in [(2.6, 6.0), (2.5, 4.8), (3.2, 6.8)]:
        ax.plot([px, px-0.6], [py, py+0.3], color=DARK_GREY, lw=1.5)
    ax.text(1.8, 6.5, "TCP Pili\n(Adherence to\nenterocytes)", ha="center", va="center", fontsize=7.2, fontweight="bold", color=DARK_GREY)

    # Secretion of Choleragen enterotoxin
    for tx, ty in [(6.0, 3.0), (5.4, 2.6), (6.6, 2.8)]:
        ax.plot(tx, ty, "*", color=YELLOW_ACCENT, markersize=8)
    ax.annotate("Choleragen Toxin Secreted\ninto Intestinal Lumen", xy=(6.0, 2.8), xytext=(6.5, 1.5),
                arrowprops=dict(arrowstyle="->", color=YELLOW_ACCENT, lw=2),
                fontsize=8, fontweight="bold", color=YELLOW_ACCENT)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_2.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.3: Choleragen Enterotoxin Molecular Mechanism
# -----------------------------------------------------------------------------
def generate_fig10_3():
    fig, ax = plt.subplots(figsize=(8.5, 6), dpi=300)
    set_plot_style(ax, "Fig. 10.3: Molecular Mechanism of Choleragen Action in Intestinal Enterocytes")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Lumen on top
    ax.add_patch(patches.Rectangle((0.5, 7.5), 9.0, 2.0, facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5))
    ax.text(5.0, 8.8, "INTESTINAL LUMEN (Choleragen Toxin Present)", ha="center", va="center", fontsize=9, fontweight="bold", color=STEEL_BLUE)

    # Enterocyte Apical Membrane (6.5 to 7.5) with microvilli
    for x in np.linspace(0.8, 9.2, 28):
        ax.plot([x, x, x+0.15, x+0.15], [6.8, 7.5, 7.5, 6.8], color=NAVY, lw=1.5)
    ax.text(1.2, 7.0, "Apical Brush Border", ha="left", va="center", fontsize=7.5, fontweight="bold", color=NAVY)

    # Choleragen Toxin Binding
    ax.add_patch(patches.Circle((2.5, 7.8), 0.35, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.5))
    ax.text(2.5, 7.8, "CT", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)
    ax.text(2.5, 8.4, "Choleragen (AB5 Toxin)\nBinds GM1 Ganglioside", ha="center", va="center", fontsize=7, fontweight="bold", color=CRIMSON)

    # Enterocyte Cytoplasm (1.8 to 6.8)
    ax.add_patch(patches.Rectangle((0.5, 1.8), 9.0, 5.0, facecolor="#fff7ed", edgecolor=NAVY, lw=1.5))
    ax.text(1.0, 6.4, "ENTEROCYTE CYTOPLASM", ha="left", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # Subunit A entry & G-protein ADP-ribosylation
    ax.text(2.8, 5.5, "1. A1 Subunit Translocates into Cytosol\n2. ADP-ribosylates Gsα Protein\n   (locks Gs in permanently ACTIVE state)",
            ha="left", va="center", fontsize=7.5, color=DARK_GREY)

    # Adenylate Cyclase Activation & cAMP
    ac_box = patches.FancyBboxPatch((2.5, 3.2), 3.2, 1.4, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5)
    ax.add_patch(ac_box)
    ax.text(4.1, 4.1, "ADENYLATE CYCLASE ACTIVATED", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)
    ax.text(4.1, 3.6, "ATP  ====>  cAMP (Massive Elevation)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # PKA & CFTR Opening
    cftr_box = patches.FancyBboxPatch((6.8, 6.2), 2.2, 1.8, boxstyle="round,pad=0.2", facecolor="#dbeafe", edgecolor=STEEL_BLUE, lw=1.5)
    ax.add_patch(cftr_box)
    ax.text(7.9, 7.2, "CFTR CHANNEL", ha="center", va="center", fontsize=7.5, fontweight="bold", color=STEEL_BLUE)
    ax.text(7.9, 6.6, "Phosphorylated by PKA;\nPermanently OPENED!", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Efflux arrows into lumen
    ax.annotate("Massive Cl- Efflux", xy=(7.5, 8.4), xytext=(7.5, 7.2),
                arrowprops=dict(arrowstyle="->", color=STEEL_BLUE, lw=2.5),
                fontsize=8, fontweight="bold", color=STEEL_BLUE)
    ax.annotate("Na+ follows Cl- (electrical)", xy=(8.5, 8.4), xytext=(8.5, 7.2),
                arrowprops=dict(arrowstyle="->", color=YELLOW_ACCENT, lw=2),
                fontsize=7.5, fontweight="bold", color=YELLOW_ACCENT)

    # Osmotic Water Loss Banner
    water_box = patches.FancyBboxPatch((0.5, 0.4), 9.0, 1.2, boxstyle="round,pad=0.1", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.8)
    ax.add_patch(water_box)
    ax.text(5.0, 1.1, "OSMOTIC EFFLUX: Water moves from blood & tissues into lumen down water potential gradient", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)
    ax.text(5.0, 0.65, "Results in: Profuse watery diarrhoea ('rice-water stools'), hypovolaemic shock, rapid fatal dehydration", ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_3.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.4: Oral Rehydration Therapy (ORT) Mechanism
# -----------------------------------------------------------------------------
def generate_fig10_4():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 10.4: Physiological Basis of Oral Rehydration Therapy (SGLT-1 Cotransport)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Lumen (Left, 0.5 to 3.0)
    ax.add_patch(patches.Rectangle((0.5, 1.5), 2.5, 7.5, facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5))
    ax.text(1.75, 8.4, "INTESTINAL\nLUMEN", ha="center", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)
    ax.text(1.75, 6.8, "Oral Rehydration\nSolution (ORS):\n• Glucose (75 mM)\n• Na+ (75 mM)\n• Cl- (65 mM)\n• K+ (20 mM)\n• Citrate (10 mM)",
            ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Enterocyte (Middle, 3.5 to 7.0)
    ax.add_patch(patches.Rectangle((3.5, 1.5), 3.5, 7.5, facecolor="#fff7ed", edgecolor=NAVY, lw=1.5))
    ax.text(5.25, 8.4, "ENTEROCYTE\nCYTOPLASM", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)

    # Blood Capillary (Right, 7.5 to 9.5)
    ax.add_patch(patches.Rectangle((7.5, 1.5), 2.0, 7.5, facecolor="#fee2e2", edgecolor=RED_VESSEL, lw=1.5))
    ax.text(8.5, 8.4, "BLOOD\nCAPILLARY", ha="center", va="center", fontsize=8.5, fontweight="bold", color=RED_VESSEL)

    # Apical SGLT-1 Transporter (at 3.5)
    ax.add_patch(patches.Ellipse((3.5, 5.5), 0.8, 1.4, facecolor="#fed7aa", edgecolor=NAVY, lw=1.5))
    ax.text(3.5, 5.5, "SGLT-1\n(Na+/Gluc)", ha="center", va="center", fontsize=6.5, fontweight="bold", color=NAVY)

    # Cotransport arrow: Lumen -> Enterocyte
    ax.annotate("Na+ & Glucose\nCotransport\n(1:1 stoichiometry)", xy=(4.5, 5.5), xytext=(2.2, 5.5),
                arrowprops=dict(arrowstyle="->", color=GREEN_ACCENT, lw=2.5),
                fontsize=7.5, fontweight="bold", color=GREEN_ACCENT)

    # Basolateral Na+/K+ ATPase (at 7.0)
    ax.add_patch(patches.Ellipse((7.0, 5.5), 0.8, 1.4, facecolor="#fca5a5", edgecolor=CRIMSON, lw=1.5))
    ax.text(7.0, 5.5, "Na+/K+\nATPase", ha="center", va="center", fontsize=6.5, fontweight="bold", color=CRIMSON)

    # Arrow to blood
    ax.annotate("3 Na+ pumped out\n(ATP used)", xy=(7.9, 5.5), xytext=(6.2, 5.5),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2),
                fontsize=7, fontweight="bold", color=CRIMSON)

    # GLUT2 (Glucose exit)
    ax.annotate("Glucose exit\nvia GLUT2", xy=(7.9, 3.8), xytext=(5.5, 3.8),
                arrowprops=dict(arrowstyle="->", color=STEEL_BLUE, lw=2),
                fontsize=7, color=STEEL_BLUE)

    # Osmosis of water (The crucial clinical point!)
    ax.annotate("WATER FOLLOWS BY OSMOSIS\ndown water potential gradient (Ψ)", xy=(8.2, 2.5), xytext=(1.8, 2.5),
                arrowprops=dict(arrowstyle="->", color=BLUE_VESSEL, lw=3),
                fontsize=8, fontweight="bold", color=BLUE_VESSEL)

    # Summary box at bottom
    bot_box = patches.FancyBboxPatch((0.5, 0.3), 9.0, 0.9, boxstyle="round,pad=0.1", facecolor="#dcfce7", edgecolor=GREEN_ACCENT, lw=1.5)
    ax.add_patch(bot_box)
    ax.text(5.0, 0.75, "WHY ORT SUCCEEDS: SGLT-1 cotransporters remain completely undamaged by choleragen toxin!", ha="center", va="center", fontsize=7.5, fontweight="bold", color=GREEN_ACCENT)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_4.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.5: Complete Life Cycle of Plasmodium
# -----------------------------------------------------------------------------
def generate_fig10_5():
    fig, ax = plt.subplots(figsize=(9, 6), dpi=300)
    set_plot_style(ax, "Fig. 10.5: Complex Life Cycle of Plasmodium (Human Host & Anopheles Vector)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Zone 1: Mosquito Vector (Top, 6.5 to 10)
    ax.add_patch(patches.Rectangle((0.5, 6.5), 9.0, 3.2, facecolor="#fef9c3", edgecolor="#ca8a04", lw=1.5))
    ax.text(5.0, 9.4, "MOSQUITO VECTOR (Female Anopheles) — Sexual Reproduction", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#854d0e")
    ax.text(2.0, 8.2, "1. Ingestion of\ngametocytes in\nblood meal", ha="center", va="center", fontsize=7.2, color=DARK_GREY)
    ax.text(5.0, 8.2, "2. Exflagellation &\nfertilisation in gut ->\nookinete -> oocyst", ha="center", va="center", fontsize=7.2, color=DARK_GREY)
    ax.text(8.0, 8.2, "3. Sporozoites\nmigrate to\nsalivary glands", ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Transmission arrow down: Mosquito bite -> Human
    ax.annotate("Injected with saliva\nduring blood meal", xy=(2.0, 5.8), xytext=(2.0, 6.8),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.5),
                fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Zone 2: Human Liver Stage (Middle Left, 3.2 to 6.2)
    ax.add_patch(patches.Rectangle((0.5, 3.2), 4.2, 3.0, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5))
    ax.text(2.6, 5.8, "HUMAN LIVER (Hepatic Schizogony)", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)
    ax.text(2.6, 4.5, "• Sporozoites invade hepatocytes\n• Asexual schizogony (7–10 days)\n• Each liver cell yields 10,000–40,000\n  MEROZOITES\n• Hepatocytes lyse, releasing merozoites",
            ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Transition: Liver -> Erythrocytes
    ax.annotate("", xy=(5.3, 4.5), xytext=(4.7, 4.5), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5))

    # Zone 3: Human Blood Stage (Middle Right, 3.2 to 6.2)
    ax.add_patch(patches.Rectangle((5.3, 3.2), 4.2, 3.0, facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5))
    ax.text(7.4, 5.8, "HUMAN ERYTHROCYTES (Erythrocytic Cycle)", ha="center", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE)
    ax.text(7.4, 4.5, "• Merozoites invade RBCs\n• Ring stage -> Trophozoite -> Schizont\n• RBC lysis releases merozoites, toxins,\n  haemozoin (fever paroxysm, chills!)\n• Repeated every 48 or 72 hours",
            ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Transition down: Some merozoites differentiate into gametocytes
    ax.annotate("Differentiation into male/female gametocytes", xy=(7.4, 2.5), xytext=(7.4, 3.2),
                arrowprops=dict(arrowstyle="->", color="#854d0e", lw=2),
                fontsize=7, color="#854d0e")

    # Uptake arrow back up to mosquito
    ax.annotate("Mosquito takes blood meal containing gametocytes", xy=(8.5, 6.8), xytext=(8.5, 2.5),
                arrowprops=dict(arrowstyle="->", color="#ca8a04", lw=2.5),
                fontsize=7.2, fontweight="bold", color="#854d0e")

    # Bottom Challenges box
    bot_box = patches.FancyBboxPatch((0.5, 0.4), 9.0, 1.6, boxstyle="round,pad=0.1", facecolor="#f1f5f9", edgecolor=NAVY, lw=1.5)
    ax.add_patch(bot_box)
    ax.text(5.0, 1.6, "WHY MALARIA IS SO DIFFICULT TO ERADICATE", ha="center", va="center", fontsize=8, fontweight="bold", color=NAVY)
    ax.text(5.0, 0.9, "• Intracellular stages (liver & RBCs) hide parasite from circulating antibodies\n• Antigenic variation (PfEMP1 surface proteins constantly mutate)\n• Vector resistance to insecticides (pyrethroids) & parasite resistance to drugs (chloroquine, ACTs)",
            ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_5.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.6: Erythrocytic Schizogony & Cyclical Fever
# -----------------------------------------------------------------------------
def generate_fig10_6():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: Erythrocytic Stages inside RBC
    set_plot_style(ax1, "Erythrocytic Schizogony Cycle")
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)
    ax1.axis("off")

    ax1.add_patch(patches.Circle((0, 0), 4.2, facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5))
    ax1.text(0, 3.4, "Invasion of RBC\nby Merozoite", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # 4 stages clockwise
    # 1. Ring form (Top right)
    ax1.add_patch(patches.Circle((2.2, 1.8), 0.8, facecolor="white", edgecolor=NAVY, lw=1.2))
    ax1.plot(2.6, 2.2, "o", color=PURPLE_ACCENT, markersize=5)
    ax1.text(2.2, 1.8, "Ring Form\n(Trophozoite)", ha="center", va="center", fontsize=6, color=NAVY)

    # 2. Mature Schizont (Bottom right)
    ax1.add_patch(patches.Circle((2.0, -1.8), 1.0, facecolor="white", edgecolor=NAVY, lw=1.2))
    for mx, my in [(1.8, -1.6), (2.3, -1.6), (1.6, -2.0), (2.2, -2.1), (1.9, -1.3)]:
        ax1.plot(mx, my, "o", color=CRIMSON, markersize=3)
    ax1.text(2.0, -2.4, "Schizont\n(16-32 merozoites)", ha="center", va="center", fontsize=6, color=CRIMSON)

    # 3. RBC Rupture (Bottom left)
    ax1.text(-2.2, -1.8, "RBC LYSIS!\nReleases:\n• Merozoites\n• Haemozoin\n• Cytokines", ha="center", va="center", fontsize=6.8, fontweight="bold", color=CRIMSON)

    # 4. Merozoite reinfection (Top left)
    ax1.text(-2.2, 1.8, "Merozoites\ninvade new\nRBCs", ha="center", va="center", fontsize=6.8, color=NAVY)

    # Ax2: Cyclical Fever Chart
    set_plot_style(ax2, "Cyclical Fever Paroxysms (P. vivax - 48h Tertian)")
    time = np.linspace(0, 96, 500)
    # Baseline temp 37C with spikes to 40.5C at 24h, 72h
    temp = 37.0 + 0.3 * np.sin(2*np.pi*time/24)
    for spike_t in [24, 72]:
        temp += 3.5 * np.exp(-((time - spike_t)/3)**2)

    ax2.plot(time, temp, color=CRIMSON, lw=2.0)
    ax2.axhline(37.0, color=DARK_GREY, linestyle="--", lw=1)
    ax2.set_xlim(0, 96)
    ax2.set_ylim(36, 42)
    ax2.set_xlabel("Time / hours", fontsize=8.5, fontweight="bold", color=NAVY)
    ax2.set_ylabel("Body Temperature / °C", fontsize=8.5, fontweight="bold", color=NAVY)

    ax2.annotate("RBC Lysis &\nFever Spike (40.5°C)!", xy=(24, 40.6), xytext=(28, 41.2),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5),
                 fontsize=7.5, fontweight="bold", color=CRIMSON)
    ax2.annotate("48-Hour Interval\n(Tertian Fever)", xy=(72, 40.6), xytext=(55, 41.2),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5),
                 fontsize=7.5, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_6.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.7: Histopathology of Tuberculosis
# -----------------------------------------------------------------------------
def generate_fig10_7():
    fig, ax = plt.subplots(figsize=(8.5, 6), dpi=300)
    set_plot_style(ax, "Fig. 10.7: Pathogenesis of Pulmonary Tuberculosis and Tubercle Formation")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    stages = [
        ("1. Inhalation & Ingestion", "Droplet nuclei inhaled;\nM. tuberculosis engulfed\nby alveolar macrophages;\nwaxy mycolic acid prevents\nphagosome-lysosome fusion.", "#fef3c7", "#ca8a04", 0.5),
        ("2. Tubercle / Granuloma", "Macrophages, T-cells &\nepithelioid cells surround\ninfection; Ghon focus forms\nwith central caseous necrosis\n(cheese-like necrotic core).", "#fee2e2", CRIMSON, 3.6),
        ("3. Cavitation & Spread", "Immunosuppression / HIV;\ntubercle wall lyses;\nliquefied core coughed out;\nleaves cavity (cavitation);\nbacteria spread via blood.", "#eff6ff", STEEL_BLUE, 6.7)
    ]

    for title, desc, bg, edge, x_pos in stages:
        box = patches.FancyBboxPatch((x_pos, 4.2), 2.8, 5.0, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=edge, lw=1.5)
        ax.add_patch(box)
        ax.text(x_pos + 1.4, 8.8, title, ha="center", va="center", fontsize=8, fontweight="bold", color=edge)
        ax.text(x_pos + 1.4, 6.4, desc, ha="center", va="center", fontsize=7.2, color=DARK_GREY)

    # Connecting arrows
    for ax_pt in [3.35, 6.45]:
        ax.annotate("", xy=(ax_pt + 0.2, 6.7), xytext=(ax_pt, 6.7), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))

    # Bottom Clinical Protocol Box: DOTS
    bot_box = patches.FancyBboxPatch((0.5, 0.4), 9.0, 3.2, boxstyle="round,pad=0.2", facecolor="#f1f5f9", edgecolor=NAVY, lw=1.5)
    ax.add_patch(bot_box)
    ax.text(5.0, 3.2, "MANAGEMENT: DIRECTLY OBSERVED THERAPY SHORT-COURSE (DOTS)", ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.text(5.0, 1.8, "• Regimen: Combination of 4 antibiotics (Isoniazid, Rifampicin, Pyrazinamide, Ethambutol)\n• Duration: 6 to 9 months continuous therapy\n• Direct Observation: Health worker watches patient swallow pills daily to ensure 100% compliance\n• Resistance Threat: Premature cessation breeds Multi-Drug Resistant TB (MDR-TB, resistant to isoniazid &\n  rifampicin) and Extensively Drug-Resistant TB (XDR-TB)",
            ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_7.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.8: Ultrastructure of HIV
# -----------------------------------------------------------------------------
def generate_fig10_8():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    set_plot_style(ax, "Fig. 10.8: Ultrastructure of Human Immunodeficiency Virus (HIV)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Viral Phospholipid Bilayer Envelope (outer circle)
    ax.add_patch(patches.Circle((5, 5), 3.4, facecolor="#f8fafc", edgecolor=NAVY, lw=2.0))
    ax.text(5, 8.1, "Phospholipid Bilayer Envelope (Derived from host membrane)", ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Glycoprotein spikes (gp120 head + gp41 stalk)
    for angle in np.linspace(0, 360, 16, endpoint=False):
        rad = np.radians(angle)
        sx1, sy1 = 5 + 3.4 * np.cos(rad), 5 + 3.4 * np.sin(rad)
        sx2, sy2 = 5 + 4.1 * np.cos(rad), 5 + 4.1 * np.sin(rad)
        ax.plot([sx1, sx2], [sy1, sy2], color=CRIMSON, lw=2)
        ax.plot(sx2, sy2, "o", color=CRIMSON, markersize=6)
    ax.text(8.8, 8.8, "gp120 Glycoprotein Knob\n(Binds CD4 receptor)\ngp41 Transmembrane Stalk", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Matrix Protein Layer (p17)
    ax.add_patch(patches.Circle((5, 5), 2.8, facecolor="#e0e7ff", edgecolor=STEEL_BLUE, lw=1.2))
    ax.text(5, 7.3, "Matrix Protein (p17)", ha="center", va="center", fontsize=7, color=STEEL_BLUE)

    # Conical Capsid (p24)
    capsid_pts = [[4.0, 3.2], [6.0, 3.2], [5.6, 6.4], [4.4, 6.4]]
    ax.add_patch(patches.Polygon(capsid_pts, closed=True, facecolor="#fed7aa", edgecolor="#ea580c", lw=1.8))
    ax.text(5, 6.0, "Capsid (p24)", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#ea580c")

    # 2 Identical Single-Stranded RNA Genomes
    t_rna = np.linspace(0, 4*np.pi, 40)
    rx1 = 4.7 + 0.15 * np.sin(t_rna)
    ry1 = 3.6 + 0.15 * t_rna
    rx2 = 5.3 + 0.15 * np.sin(t_rna)
    ry2 = 3.6 + 0.15 * t_rna
    ax.plot(rx1, ry1, color=PURPLE_ACCENT, lw=2)
    ax.plot(rx2, ry2, color=PURPLE_ACCENT, lw=2)
    ax.text(5, 4.8, "Two Identical\nssRNA Strands", ha="center", va="center", fontsize=7, fontweight="bold", color=PURPLE_ACCENT)

    # Enzymes inside capsid: Reverse Transcriptase, Integrase, Protease
    ax.plot(4.6, 3.8, "s", color=CRIMSON, markersize=5)
    ax.plot(5.4, 3.8, "^", color=GREEN_ACCENT, markersize=5)
    ax.plot(5.0, 3.5, "D", color=YELLOW_ACCENT, markersize=5)
    ax.text(5.0, 2.2, "Viral Enzymes:\n■ Reverse Transcriptase (RT)  |  ▲ Integrase  |  ◆ Protease", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_8.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.9: HIV Replication Cycle in CD4+ T-cell
# -----------------------------------------------------------------------------
def generate_fig10_9():
    fig, ax = plt.subplots(figsize=(8.5, 6), dpi=300)
    set_plot_style(ax, "Fig. 10.9: HIV Life Cycle: Entry, Reverse Transcription, and Integration")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # T-cell Cytoplasm (1.0 to 9.0)
    ax.add_patch(patches.Rectangle((0.5, 1.0), 9.0, 7.5, facecolor="#eff6ff", edgecolor=NAVY, lw=1.5))
    ax.text(1.0, 8.1, "CD4+ T-HELPER LYMPHOCYTE CYTOPLASM", ha="left", va="center", fontsize=8, fontweight="bold", color=NAVY)

    # T-cell Nucleus (5.5 to 8.5)
    ax.add_patch(patches.Ellipse((7.0, 4.5), 3.2, 4.0, facecolor="#dbeafe", edgecolor=STEEL_BLUE, lw=1.5))
    ax.text(7.0, 6.0, "T-Cell Nucleus", ha="center", va="center", fontsize=8, fontweight="bold", color=STEEL_BLUE)

    # Step 1: Binding & Fusion (Top Left)
    ax.text(1.8, 7.2, "1. ATTACHMENT & ENTRY\n• gp120 binds CD4 & CCR5\n• Envelope fuses with cell membrane\n• Capsid released into cytoplasm", ha="left", va="center", fontsize=7, color=DARK_GREY)

    # Step 2: Reverse Transcription
    ax.text(1.8, 5.0, "2. REVERSE TRANSCRIPTION\n• Viral ssRNA ======> ds-cDNA\n• Enzyme: Reverse Transcriptase\n(Lacks proofreading -> high mutation rate!)", ha="left", va="center", fontsize=7, color=DARK_GREY)

    # Step 3: Proviral Integration (Inside Nucleus)
    ax.text(7.0, 4.5, "3. INTEGRATION\n• Viral ds-cDNA enters nucleus\n• INTEGRASE inserts cDNA into\n  host chromosome (PROVIRUS)", ha="center", va="center", fontsize=7, color=DARK_GREY)

    # Step 4: Transcription & Translation (Bottom Left)
    ax.text(1.8, 2.8, "4. TRANSCRIPTION & BUDDING\n• Host RNA polymerase transcribes viral mRNA\n• Translated into viral polyproteins (cleaved by Protease)\n• New virions bud, taking host membrane", ha="left", va="center", fontsize=7, color=DARK_GREY)

    # Antiretroviral Drug Targets (bottom)
    bot_box = patches.FancyBboxPatch((0.5, 0.2), 9.0, 0.7, boxstyle="round,pad=0.1", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.2)
    ax.add_patch(bot_box)
    ax.text(5.0, 0.55, "ANTIRETROVIRAL THERAPY (ART) TARGETS: NRTIs/NNRTIs (block RT) | Integrase Inhibitors | Protease Inhibitors", ha="center", va="center", fontsize=7.2, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_9.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.10: Clinical Progression of HIV to AIDS
# -----------------------------------------------------------------------------
def generate_fig10_10():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 10.10: Clinical Timeline: CD4 T-Cell Count vs Viral Load Progression to AIDS")

    years = np.linspace(0, 11, 300)
    # CD4 count (starts at 1000, drops acutely, rebounds to 700, then steady decline to < 200)
    cd4 = np.zeros_like(years)
    for i, y in enumerate(years):
        if y < 0.5:
            cd4[i] = 1000 - 500 * (y / 0.5)
        elif y < 2.0:
            cd4[i] = 500 + 200 * ((y - 0.5) / 1.5)
        else:
            cd4[i] = 700 - 55 * (y - 2.0)
    cd4 = np.clip(cd4, 20, 1200)

    # Viral load (RNA copies/mL, log scale: 2 to 7)
    vl = np.zeros_like(years)
    for i, y in enumerate(years):
        if y < 0.25:
            vl[i] = 2.0 + 4.5 * (y / 0.25)
        elif y < 1.5:
            vl[i] = 6.5 - 3.5 * ((y - 0.25) / 1.25)
        else:
            vl[i] = 3.0 + 0.35 * (y - 1.5)
    vl = np.clip(vl, 2, 7)

    # Plot CD4 on ax1
    line1 = ax.plot(years, cd4, color=STEEL_BLUE, lw=2.5, label="CD4+ T-cell count (cells/µL)")
    ax.set_ylabel("CD4+ T-cell Count / cells µL⁻¹", fontsize=9, fontweight="bold", color=STEEL_BLUE)
    ax.set_ylim(0, 1200)
    ax.set_xlabel("Time / years after infection", fontsize=9, fontweight="bold", color=NAVY)

    # Plot Viral Load on twin ax
    ax2 = ax.twinx()
    line2 = ax2.plot(years, vl, color=CRIMSON, lw=2.5, linestyle="--", label="HIV RNA copies/mL (log10)")
    ax2.set_ylabel("HIV RNA Copies / mL (log₁₀ scale)", fontsize=9, fontweight="bold", color=CRIMSON)
    ax2.set_ylim(1, 8)

    # AIDS threshold line at CD4 = 200
    ax.axhline(200, color=CRIMSON, linestyle=":", lw=1.8)
    ax.text(10.5, 220, "AIDS Threshold\n(< 200 cells/µL)", ha="right", va="bottom", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Clinical stages labels
    ax.axvspan(0, 1, facecolor="#fee2e2", alpha=0.3)
    ax.text(0.5, 1100, "Acute\nPhase", ha="center", va="top", fontsize=7.5, fontweight="bold", color=CRIMSON)

    ax.axvspan(1, 8.5, facecolor="#eff6ff", alpha=0.3)
    ax.text(4.5, 1100, "Clinical Latency (Asymptomatic Phase)\n(Gradual destruction of CD4 T-cells)", ha="center", va="top", fontsize=8, fontweight="bold", color=STEEL_BLUE)

    ax.axvspan(8.5, 11, facecolor="#fef2f2", alpha=0.5)
    ax.text(9.7, 1100, "AIDS\n(Opportunistic\nInfections)", ha="center", va="top", fontsize=7.5, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_10.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.11: Penicillin Mode of Action on Bacterial Cell Wall
# -----------------------------------------------------------------------------
def generate_fig10_11():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: Normal Cell Wall Synthesis
    set_plot_style(ax1, "Normal Bacterial Cell Wall Synthesis")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")

    # Polysaccharide glycan chains (horizontal)
    for y in [7.5, 5.5, 3.5]:
        ax1.plot([1.0, 9.0], [y, y], color=STEEL_BLUE, lw=4)
        ax1.text(0.8, y, "NAG-NAM", ha="right", va="center", fontsize=7, color=STEEL_BLUE)

    # Peptide cross-links (vertical)
    for x in [2.5, 5.0, 7.5]:
        ax1.plot([x, x], [7.5, 5.5], color=GREEN_ACCENT, lw=3)
        ax1.plot([x, x], [5.5, 3.5], color=GREEN_ACCENT, lw=3)
    ax1.text(5.0, 6.5, "Transpeptidase Cross-Links\n(Strong Peptidoglycan Mesh)", ha="center", va="center", fontsize=7.5, fontweight="bold", color=GREEN_ACCENT)

    ax1.text(5.0, 1.8, "• Transpeptidase forms peptide cross-links\n• Rigid lattice withstands internal turgor\n  pressure (up to 20 atm)",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Ax2: In Presence of Penicillin
    set_plot_style(ax2, "Action of Penicillin: Osmotic Lysis")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")

    # Polysaccharide chains unlinked
    for y in [7.5, 5.5, 3.5]:
        ax2.plot([1.0, 9.0], [y, y], color=STEEL_BLUE, lw=4)

    # Broken/absent cross-links
    ax2.plot(5.0, 5.5, "x", color=CRIMSON, markersize=14, markeredgewidth=3)
    ax2.text(5.0, 6.5, "TRANSPEPTIDASE INHIBITED!\nNo Cross-Links Formed", ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    # Weakened wall & osmotic entry
    ax2.annotate("Water enters by OSMOSIS\ndown water potential gradient", xy=(5.0, 4.0), xytext=(5.0, 2.5),
                arrowprops=dict(arrowstyle="->", color=BLUE_VESSEL, lw=2.5),
                fontsize=7.5, fontweight="bold", color=BLUE_VESSEL, ha="center")

    ax2.text(5.0, 1.0, "CELL UNDERGOES OSMOTIC LYSIS (BURSTS)!\n(Only effective on growing bacteria synthesising new walls)",
             ha="center", va="center", fontsize=7.5, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_11.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.12: Molecular Mechanisms of Antibiotic Resistance
# -----------------------------------------------------------------------------
def generate_fig10_12():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 10.12: Four Major Molecular Mechanisms of Bacterial Antibiotic Resistance")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    cards = [
        ("1. Enzymatic Inactivation", "β-lactamase (penicillinase)\nhydrolyses the cyclic amide\nbond in the β-lactam ring,\ninactivating penicillin.", "#fee2e2", CRIMSON, 0.5, 5.2),
        ("2. Altered Target Site", "Mutations in transpeptidase\ngene alter active site shape;\nantibiotic cannot bind, but\npeptidoglycan cross-linking continues.", "#eff6ff", STEEL_BLUE, 5.3, 5.2),
        ("3. Active Efflux Pumps", "Multidrug efflux pumps (efflux\ntransporters) actively pump\nantibiotics out of cytoplasm\nbefore reaching targets.", "#fef3c7", "#ca8a04", 0.5, 0.5),
        ("4. Decreased Permeability", "Downregulation or structural\nmutation of outer membrane\nporin proteins blocks antibiotic\nentry into periplasm.", "#f0fdf4", GREEN_ACCENT, 5.3, 0.5)
    ]

    for title, desc, bg, edge, x, y in cards:
        box = patches.FancyBboxPatch((x, y), 4.2, 4.2, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=edge, lw=1.5)
        ax.add_patch(box)
        ax.text(x + 2.1, y + 3.6, title, ha="center", va="center", fontsize=8.5, fontweight="bold", color=edge)
        ax.text(x + 2.1, y + 1.8, desc, ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_12.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.13: Horizontal vs Vertical Transmission of Resistance
# -----------------------------------------------------------------------------
def generate_fig10_13():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5), dpi=300)

    # Ax1: Vertical Transmission
    set_plot_style(ax1, "Vertical Transmission (Binary Fission)")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis("off")

    c1 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#eff6ff", edgecolor=STEEL_BLUE, lw=1.5)
    ax1.add_patch(c1)
    ax1.text(5.0, 8.5, "VERTICAL INHERITANCE", ha="center", va="center", fontsize=8.5, fontweight="bold", color=STEEL_BLUE)
    ax1.text(5.0, 5.0, "• Resistant parent bacterium divides\n  asexually via BINARY FISSION\n\n• Chromosomal DNA and R-plasmids\n  replicate semi-conservatively\n\n• Identical copies distributed to each\n  daughter cell\n\n• Entire clonal lineage inherits resistance\n\n• Operates WITHIN the same species",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    # Ax2: Horizontal Transmission
    set_plot_style(ax2, "Horizontal Transmission (Conjugation)")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")

    c2 = patches.FancyBboxPatch((0.5, 0.5), 9.0, 9.0, boxstyle="round,pad=0.2", facecolor="#fee2e2", edgecolor=CRIMSON, lw=1.5)
    ax2.add_patch(c2)
    ax2.text(5.0, 8.5, "HORIZONTAL CONJUGATION", ha="center", va="center", fontsize=8.5, fontweight="bold", color=CRIMSON)
    ax2.text(5.0, 5.0, "• Donor cell (F+) extends a SEX PILUS\n  to make contact with recipient (F-)\n\n• Pilus retracts, forming conjugation bridge\n\n• R-plasmid strand nicked and transferred\n  via rolling-circle replication\n\n• Recipient synthesises complementary strand\n  and becomes resistant (F+)\n\n• Can cross DIFFERENT bacterial species!\n  (e.g. harmless gut flora -> pathogen)",
             ha="center", va="center", fontsize=7.5, color=DARK_GREY)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_13.png"), dpi=300)
    plt.close(fig)

# -----------------------------------------------------------------------------
# Fig 10.14: Selection Pressure Dynamics in Bacterial Population
# -----------------------------------------------------------------------------
def generate_fig10_14():
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    set_plot_style(ax, "Fig. 10.14: Natural Selection of Antibiotic Resistance under Treatment Pressure")

    time = np.linspace(0, 14, 300)
    # Sensitive population (starts high, crashes when antibiotic given at day 2)
    sens = np.zeros_like(time)
    for i, t in enumerate(time):
        if t < 2:
            sens[i] = 100
        else:
            sens[i] = 100 * np.exp(-1.5 * (t - 2))

    # Resistant population (rare initially, expands exponentially due to selection)
    res = np.zeros_like(time)
    for i, t in enumerate(time):
        if t < 2:
            res[i] = 0.5
        else:
            res[i] = 0.5 * np.exp(0.55 * (t - 2))
    res = np.clip(res, 0, 100)

    ax.plot(time, sens, color=STEEL_BLUE, lw=2.5, label="Susceptible Bacteria (Killed by antibiotic)")
    ax.plot(time, res, color=CRIMSON, lw=2.5, label="Resistant Mutants (Survive & multiply)")

    # Antibiotic administration shaded zone
    ax.axvspan(2, 14, facecolor="#fee2e2", alpha=0.3)
    ax.text(8.0, 92, "ANTIBIOTIC SELECTION PRESSURE APPLIED", ha="center", va="center", fontsize=8, fontweight="bold", color=CRIMSON)

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 110)
    ax.set_xlabel("Time / days", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.set_ylabel("Percentage of Bacterial Population / %", fontsize=8.5, fontweight="bold", color=NAVY)
    ax.legend(loc="center right", fontsize=8)

    ax.annotate("Random Mutation confers resistance\nPRIOR to antibiotic exposure!", xy=(1.5, 2), xytext=(2.5, 20),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5),
                fontsize=7.5, color=DARK_GREY)

    ax.annotate("Superbug population dominates\n(Treatment failure)", xy=(12, 95), xytext=(9, 70),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.5),
                fontsize=7.5, fontweight="bold", color=CRIMSON)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "fig10_14.png"), dpi=300)
    plt.close(fig)

def main():
    print("Generating 14 vector diagrams for Topic 10: Infectious Diseases...")
    generate_fig10_1()
    generate_fig10_2()
    generate_fig10_3()
    generate_fig10_4()
    generate_fig10_5()
    generate_fig10_6()
    generate_fig10_7()
    generate_fig10_8()
    generate_fig10_9()
    generate_fig10_10()
    generate_fig10_11()
    generate_fig10_12()
    generate_fig10_13()
    generate_fig10_14()
    print("All 14 Topic 10 figures generated successfully in 300 DPI!")

if __name__ == "__main__":
    main()
