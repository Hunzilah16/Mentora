"""
Cambridge International AS Level Biology (9700)
Topic 3: Enzymes — High-Precision Publication-Quality Diagram Generator
Generates 14 high-resolution 300 DPI figures for Topic 3:
1.  fig3_1_activation_energy_profile.png
2.  fig3_2_induced_fit_mechanism.png
3.  fig3_3_reaction_progress_catalase.png
4.  fig3_4_starch_amylase_colorimeter.png
5.  fig3_5_temperature_effect_denaturation.png
6.  fig3_6_ph_effect_bell_curve.png
7.  fig3_7_enzyme_concentration_effect.png
8.  fig3_8_substrate_concentration_saturation.png
9.  fig3_9_michaelis_menten_km_vmax.png
10. fig3_10_competitive_inhibition_kinetics.png
11. fig3_11_non_competitive_allosteric.png
12. fig3_12_lineweaver_burk_double_reciprocal.png
13. fig3_13_immobilised_enzymes_alginate.png
14. fig3_14_end_product_allosteric_feedback.png
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
# FIG 3.1: ACTIVATION ENERGY PROFILE
# ==============================================================================
def generate_fig3_1(filename="fig3_1_activation_energy_profile.png"):
    fig, ax = plt.subplots(figsize=(7.6, 4.4), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    ax.text(50, 96, "Energy Profile of an Exergonic Reaction With and Without Enzyme",
            fontsize=8.8, fontweight='bold', color=NAVY, ha='center')
    
    # Axes
    ax.annotate("", xy=(8, 90), xytext=(8, 12), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5))
    ax.text(5, 52, "Free Energy (G) / kJ mol⁻¹", fontsize=7.2, fontweight='bold', color=DARK_GREY, rotation=90, va='center')
    
    ax.annotate("", xy=(95, 12), xytext=(8, 12), arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.5))
    ax.text(52, 6, "Progress of Reaction", fontsize=7.2, fontweight='bold', color=DARK_GREY, ha='center')

    # Substrate plateau (y = 45)
    ax.plot([12, 28], [45, 45], color=NAVY, linewidth=2.2)
    ax.text(20, 48, "Substrates (S)", fontsize=7.8, fontweight='bold', color=NAVY, ha='center')

    # Product plateau (y = 22)
    ax.plot([72, 92], [22, 22], color=NAVY, linewidth=2.2)
    ax.text(82, 25, "Products (P)", fontsize=7.8, fontweight='bold', color=NAVY, ha='center')

    # Uncatalysed curve (peaks at y = 84)
    x_uncat = np.linspace(28, 72, 100)
    y_uncat = 45 + 39 * np.sin(np.pi * (x_uncat - 28) / 44) - (x_uncat - 28) * 0.52
    ax.plot(x_uncat, y_uncat, 'r--', linewidth=1.8, label="Uncatalysed reaction")

    # Catalysed curve (peaks at y = 62)
    x_cat = np.linspace(28, 72, 100)
    y_cat = 45 + 17 * np.sin(np.pi * (x_cat - 28) / 44) - (x_cat - 28) * 0.52
    ax.plot(x_cat, y_cat, color="#2b75d6", linewidth=2.2, label="Enzyme-catalysed reaction")

    # Activation energies
    # Ea uncatalysed
    ax.plot([48, 48], [45, 83.5], 'r-', linewidth=1.2)
    ax.plot([45, 51], [83.5, 83.5], 'r-', linewidth=1.0)
    ax.annotate("Ea without enzyme\n(uncatalysed)", xy=(48, 70), xytext=(24, 76),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.5, fontweight='bold', color=CRIMSON)

    # Ea catalysed
    ax.plot([54, 54], [45, 61.5], color="#2b75d6", linewidth=1.4)
    ax.plot([51, 57], [61.5, 61.5], color="#2b75d6", linewidth=1.0)
    ax.annotate("Ea with enzyme\n(significantly lowered)", xy=(54, 54), xytext=(66, 68),
                arrowprops=dict(arrowstyle="->", color="#2b75d6", lw=1.0),
                fontsize=6.5, fontweight='bold', color="#2b75d6")

    # Delta G (overall free energy change)
    ax.plot([86, 86], [22, 45], 'k:', linewidth=1.4)
    ax.plot([83, 89], [45, 45], 'k:', linewidth=1.0)
    ax.annotate("ΔG (overall free energy)\nUnchanged by enzyme", xy=(86, 33.5), xytext=(72, 46),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=0.9),
                fontsize=6.2, fontweight='bold', color=DARK_GREY)

    ax.legend(loc="upper right", fontsize=6.8, framealpha=0.9)
    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.2: INDUCED-FIT MECHANISM
# ==============================================================================
def generate_fig3_2(filename="fig3_2_induced_fit_mechanism.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.0), dpi=300)
    
    for ax, title in zip([ax1, ax2], ["A: Lock-and-Key Model (Rigid)", "B: Induced-Fit Model (Dynamic)"]):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 70)
        ax.axis('off')
        ax.set_title(title, fontsize=8.2, fontweight='bold', color=NAVY, pad=4)

    # Panel 1: Lock and key
    # Enzyme body
    e_coords1 = [(20, 20), (20, 45), (42, 45), (42, 30), (58, 30), (58, 45), (80, 45), (80, 20)]
    poly1 = Polygon(e_coords1, closed=True, facecolor="#e8f0fe", edgecolor=NAVY, lw=1.6)
    ax1.add_patch(poly1)
    ax1.text(50, 23, "Enzyme", fontsize=7.5, fontweight='bold', color=NAVY, ha='center')
    ax1.text(50, 36, "Rigid Active Site", fontsize=6.2, color=CRIMSON, ha='center')

    # Complementary Substrate above
    s_coords1 = [(43, 52), (43, 62), (57, 62), (57, 52)]
    poly_s1 = Polygon(s_coords1, closed=True, facecolor="#fce8e6", edgecolor=CRIMSON, lw=1.4)
    ax1.add_patch(poly_s1)
    ax1.text(50, 56, "Substrate", fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')
    ax1.text(50, 10, "• Active site precisely complementary\n• No conformational change required\n• Substrate fits like key into lock",
             fontsize=6.2, color=DARK_GREY, ha='center')

    # Panel 2: Induced fit
    # Enzyme with slightly non-matching cleft
    e_coords2 = [(20, 20), (20, 45), (40, 45), (45, 34), (55, 34), (60, 45), (80, 45), (80, 20)]
    poly2 = Polygon(e_coords2, closed=True, facecolor="#e8f0fe", edgecolor=NAVY, lw=1.6)
    ax2.add_patch(poly2)
    ax2.text(50, 23, "Enzyme", fontsize=7.5, fontweight='bold', color=NAVY, ha='center')

    # Substrate
    s_coords2 = [(43, 52), (43, 62), (57, 62), (57, 52)]
    poly_s2 = Polygon(s_coords2, closed=True, facecolor="#fce8e6", edgecolor=CRIMSON, lw=1.4)
    ax2.add_patch(poly_s2)
    ax2.text(50, 56, "Substrate", fontsize=6.8, fontweight='bold', color=CRIMSON, ha='center')

    # Conformational change arrows
    ax2.annotate("", xy=(47, 36), xytext=(40, 42), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2))
    ax2.annotate("", xy=(53, 36), xytext=(60, 42), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.2))
    ax2.text(50, 39, "Moulds around\nsubstrate", fontsize=6.0, fontweight='bold', color=CRIMSON, ha='center')
    ax2.text(50, 10, "• Active site not fully complementary initially\n• Substrate binding induces conformational strain\n• Strains substrate bonds, lowering Ea",
             fontsize=6.2, color=DARK_GREY, ha='center')

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.3: REACTION PROGRESS CURVE (CATALASE O2 VOLUME)
# ==============================================================================
def generate_fig3_3(filename="fig3_3_reaction_progress_catalase.png"):
    fig, ax = plt.subplots(figsize=(7.6, 4.2), dpi=300)
    
    t = np.linspace(0, 180, 200)
    # Exponential plateau curve: V(t) = Vmax * (1 - exp(-k*t))
    v = 48 * (1 - np.exp(-0.028 * t))
    
    ax.plot(t, v, color=NAVY, linewidth=2.2, label="Volume of O₂ collected")
    
    # Tangent at t = 0 (Initial Rate)
    # Initial rate = 48 * 0.028 = 1.344 cm3/s
    t_tan = np.linspace(0, 40, 50)
    v_tan = 1.344 * t_tan
    ax.plot(t_tan, v_tan, 'r--', linewidth=1.6, label="Initial rate tangent (t = 0 s)")
    
    # Tangent calculation box
    ax.plot([30, 30], [0, 1.344*30], 'k:', lw=1.0)
    ax.plot([0, 30], [1.344*30, 1.344*30], 'k:', lw=1.0)
    ax.annotate("Initial Rate =\nΔV / Δt = 40.3 / 30\n= 1.34 cm³ s⁻¹", xy=(15, 20), xytext=(28, 12),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.8, fontweight='bold', color=CRIMSON,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f2", ec=CRIMSON, lw=0.8))

    # Rate decreases annotation
    ax.annotate("Rate slows down:\nSubstrate (H₂O₂) depleted\nFewer ES collisions", xy=(90, 44), xytext=(70, 30),
                arrowprops=dict(arrowstyle="->", color=DARK_GREY, lw=1.0),
                fontsize=6.5, color=DARK_GREY)

    # Plateau annotation
    ax.plot([140, 180], [48, 48], 'b:', lw=1.0)
    ax.annotate("Plateau: Reaction complete\nAll H₂O₂ converted to H₂O + O₂", xy=(150, 48), xytext=(120, 41),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                fontsize=6.5, fontweight='bold', color=NAVY)

    ax.set_xlim(0, 190)
    ax.set_ylim(0, 55)
    ax.set_xlabel("Time / s", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Volume of Oxygen (O₂) Collected / cm³", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_title("Progress Curve of Hydrogen Peroxide Decomposition by Catalase",
                 fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc="lower right", fontsize=6.8, framealpha=0.9)
    ax.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.4: STARCH AMYLASE COLORIMETER TRANSMISSION
# ==============================================================================
def generate_fig3_4(filename="fig3_4_starch_amylase_colorimeter.png"):
    fig, ax = plt.subplots(figsize=(7.6, 4.0), dpi=300)
    
    t = np.linspace(0, 120, 200)
    # Starch breakdown: Absorbance decreases from 1.0 to 0.05
    # Transmission increases from 10% to 90%
    transmission = 10 + 80 * (1 - np.exp(-0.035 * t))
    
    ax.plot(t, transmission, color="#1a8754", linewidth=2.2, label="% Transmission (yellow filter 580 nm)")
    
    # Endpoint / Achromic point
    ax.plot([0, 120], [88, 88], 'r:', linewidth=1.2)
    ax.annotate("Achromic point (~90 s)\nStarch fully hydrolysed to maltose\nNo iodine-starch complex",
                xy=(90, 87), xytext=(55, 65),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.8, fontweight='bold', color=CRIMSON,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f2", ec=CRIMSON, lw=0.8))

    ax.set_xlim(0, 130)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Incubation Time / s", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Light Transmission / %", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_title("Amylase Hydrolysis of Starch Monitored by Colorimetry",
                 fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc="lower right", fontsize=6.8, framealpha=0.9)
    ax.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.5: TEMPERATURE EFFECT & DENATURATION
# ==============================================================================
def generate_fig3_5(filename="fig3_5_temperature_effect_denaturation.png"):
    fig, ax = plt.subplots(figsize=(7.6, 4.2), dpi=300)
    
    temp = np.linspace(0, 75, 200)
    # Rate curve: product of kinetic activation and denaturation
    rate = (temp**2.2 * np.exp(-temp / 13.0))
    rate = (rate / np.max(rate)) * 100
    
    ax.plot(temp, rate, color=NAVY, linewidth=2.4)
    
    # Optimum temp line
    opt_temp = temp[np.argmax(rate)]
    ax.plot([opt_temp, opt_temp], [0, 100], 'r--', linewidth=1.4)
    ax.plot(opt_temp, 100, 'o', color=CRIMSON, markersize=6)
    ax.annotate(f"Optimum Temperature (~{opt_temp:.0f} °C)\nMaximum kinetic energy\nbefore denaturation dominates",
                xy=(opt_temp, 100), xytext=(opt_temp - 24, 82),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.8, fontweight='bold', color=CRIMSON,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f2", ec=CRIMSON, lw=0.8))

    # Q10 arrow (0 to 30 deg)
    ax.annotate("Rate doubles every 10 °C (Q₁₀ ≈ 2)\nIncreased kinetic energy\nMore frequent successful collisions",
                xy=(22, 28), xytext=(6, 52),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                fontsize=6.5, color=NAVY)

    # Denaturation zone (> 45 deg)
    ax.annotate("Thermal Denaturation (> 45 °C)\nViolent vibrations break\nhydrogen and ionic bonds\nActive site tertiary shape lost",
                xy=(52, 42), xytext=(52, 60),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.5, fontweight='bold', color=CRIMSON)

    ax.set_xlim(0, 75)
    ax.set_ylim(0, 110)
    ax.set_xlabel("Temperature / °C", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Rate of Reaction / Arbitrary Units", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_title("Effect of Temperature on the Rate of an Enzyme-Catalysed Reaction",
                 fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.6: PH EFFECT ON PEPSIN, SALIVARY AMYLASE, TRYPSIN
# ==============================================================================
def generate_fig3_6(filename="fig3_6_ph_effect_bell_curve.png"):
    fig, ax = plt.subplots(figsize=(7.8, 4.2), dpi=300)
    
    ph = np.linspace(0, 12, 300)
    
    # Gaussian bell curves for 3 digestive enzymes
    # Pepsin: opt 2.0, sigma 0.8
    r_pepsin = 100 * np.exp(-((ph - 2.0)**2) / (2 * 0.75**2))
    # Salivary amylase: opt 6.8, sigma 1.0
    r_amylase = 100 * np.exp(-((ph - 6.8)**2) / (2 * 0.9**2))
    # Trypsin: opt 8.5, sigma 1.1
    r_trypsin = 100 * np.exp(-((ph - 8.5)**2) / (2 * 1.0**2))
    
    ax.plot(ph, r_pepsin, color=CRIMSON, linewidth=2.0, label="Pepsin (Gastric protease, opt pH 2.0)")
    ax.plot(ph, r_amylase, color="#2b75d6", linewidth=2.0, label="Salivary Amylase (opt pH 6.8)")
    ax.plot(ph, r_trypsin, color="#1a8754", linewidth=2.0, label="Trypsin (Duodenal protease, opt pH 8.5)")

    ax.annotate("Stomach acid\npH 1.5–2.0", xy=(2.0, 100), xytext=(0.8, 80),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.5, fontweight='bold', color=CRIMSON)

    ax.annotate("Mouth / Saliva\npH ~6.8", xy=(6.8, 100), xytext=(5.5, 82),
                arrowprops=dict(arrowstyle="->", color="#2b75d6", lw=1.0),
                fontsize=6.5, fontweight='bold', color="#2b75d6")

    ax.annotate("Duodenum\npH 8.0–8.5", xy=(8.5, 100), xytext=(9.2, 82),
                arrowprops=dict(arrowstyle="->", color="#1a8754", lw=1.0),
                fontsize=6.5, fontweight='bold', color="#1a8754")

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 115)
    ax.set_xlabel("pH", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Enzyme Activity / % Maximum", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_title("Effect of pH on the Catalytic Activity of Three Human Digestive Enzymes",
                 fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc="upper right", fontsize=6.8, framealpha=0.9)
    ax.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.7: ENZYME CONCENTRATION EFFECT
# ==============================================================================
def generate_fig3_7(filename="fig3_7_enzyme_concentration_effect.png"):
    fig, ax = plt.subplots(figsize=(7.6, 4.0), dpi=300)
    
    e_conc = np.linspace(0, 10, 100)
    
    # Excess substrate: linear throughout
    rate_excess = 10 * e_conc
    ax.plot(e_conc, rate_excess, color=NAVY, linewidth=2.2, label="Substrate in excess (linear: [E] is limiting)")

    # Limiting substrate: plateaus above [E] = 5
    rate_limit = 100 * (e_conc / (e_conc + 3.0))
    rate_limit = rate_limit * (80 / np.max(rate_limit))
    ax.plot(e_conc, rate_limit, 'r--', linewidth=2.0, label="Substrate limited (plateaus: [S] becomes limiting)")

    ax.annotate("Linear region:\nDouble [E] = Double rate\nMore active sites available", xy=(3.5, 35), xytext=(0.8, 55),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                fontsize=6.5, fontweight='bold', color=NAVY)

    ax.annotate("Plateau region:\nAll substrate molecules\nbound; excess active sites idle", xy=(8.0, 58), xytext=(5.8, 38),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.5, fontweight='bold', color=CRIMSON)

    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 105)
    ax.set_xlabel("Enzyme Concentration / Arbitrary Units", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Initial Rate of Reaction / Arbitrary Units", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_title("Effect of Enzyme Concentration on Initial Reaction Rate",
                 fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc="lower right", fontsize=6.8, framealpha=0.9)
    ax.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.8: SUBSTRATE CONCENTRATION SATURATION
# ==============================================================================
def generate_fig3_8(filename="fig3_8_substrate_concentration_saturation.png"):
    fig, ax = plt.subplots(figsize=(7.6, 4.2), dpi=300)
    
    s = np.linspace(0, 50, 200)
    # Michaelis-Menten: V = Vmax * S / (Km + S)
    vmax = 100
    km = 6.0
    v = vmax * s / (km + s)
    
    ax.plot(s, v, color=NAVY, linewidth=2.4)
    
    # Asymptote Vmax
    ax.plot([0, 50], [vmax, vmax], 'r--', linewidth=1.2, label=f"Vmax ({vmax} arbitrary units)")
    
    # First order region annotation
    ax.annotate("First-order kinetics:\nRate ∝ [S]\nMany active sites empty\n[S] is the limiting factor",
                xy=(4, 40), xytext=(5, 68),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                fontsize=6.5, color=NAVY)

    # Zero order region annotation
    ax.annotate("Zero-order kinetics (Saturation):\nAll active sites fully occupied (ES complex)\nEnzyme concentration is limiting factor",
                xy=(38, 92), xytext=(22, 45),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.5, fontweight='bold', color=CRIMSON)

    ax.set_xlim(0, 52)
    ax.set_ylim(0, 115)
    ax.set_xlabel("Substrate Concentration [S] / mmol dm⁻³", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Initial Rate of Reaction (V) / Arbitrary Units", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_title("Hyperbolic Saturation Curve of Reaction Rate vs Substrate Concentration",
                 fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc="lower right", fontsize=6.8, framealpha=0.9)
    ax.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.9: MICHAELIS-MENTEN KM AND VMAX DERIVATION
# ==============================================================================
def generate_fig3_9(filename="fig3_9_michaelis_menten_km_vmax.png"):
    fig, ax = plt.subplots(figsize=(7.8, 4.4), dpi=300)
    
    s = np.linspace(0, 40, 200)
    
    # Enzyme 1: High affinity (Low Km = 4.0, Vmax = 80)
    vmax1 = 80
    km1 = 4.0
    v1 = vmax1 * s / (km1 + s)
    
    # Enzyme 2: Low affinity (High Km = 14.0, Vmax = 80)
    vmax2 = 80
    km2 = 14.0
    v2 = vmax2 * s / (km2 + s)
    
    ax.plot(s, v1, color="#2b75d6", linewidth=2.2, label="Enzyme 1: Low Km (High affinity for substrate)")
    ax.plot(s, v2, color=CRIMSON, linewidth=2.2, label="Enzyme 2: High Km (Low affinity for substrate)")
    
    # Vmax and 1/2 Vmax
    ax.plot([0, 40], [80, 80], 'k--', linewidth=1.2, label="Vmax = 80 AU")
    ax.plot([0, 40], [40, 40], 'k:', linewidth=1.2, label="½ Vmax = 40 AU")
    
    # Km projections
    ax.plot([km1, km1], [0, 40], color="#2b75d6", linestyle='--', linewidth=1.4)
    ax.plot(km1, 40, 'o', color="#2b75d6", markersize=5)
    ax.annotate(f"Km (Enzyme 1) = {km1} mM\nHigher catalytic efficiency\nat low [S]",
                xy=(km1, 40), xytext=(km1 + 2, 22),
                arrowprops=dict(arrowstyle="->", color="#2b75d6", lw=1.0),
                fontsize=6.5, fontweight='bold', color="#2b75d6")

    ax.plot([km2, km2], [0, 40], color=CRIMSON, linestyle='--', linewidth=1.4)
    ax.plot(km2, 40, 's', color=CRIMSON, markersize=5)
    ax.annotate(f"Km (Enzyme 2) = {km2} mM\nRequires higher [S]\nto reach ½ Vmax",
                xy=(km2, 40), xytext=(km2 + 2, 14),
                arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                fontsize=6.5, fontweight='bold', color=CRIMSON)

    ax.set_xlim(0, 42)
    ax.set_ylim(0, 95)
    ax.set_xlabel("Substrate Concentration [S] / mmol dm⁻³", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("Initial Velocity (V) / Arbitrary Units", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_title("Derivation of Michaelis-Menten Constant (Km) and Substrate Affinity Comparison",
                 fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc="lower right", fontsize=6.8, framealpha=0.9)
    ax.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.10: COMPETITIVE INHIBITION KINETICS
# ==============================================================================
def generate_fig3_10(filename="fig3_10_competitive_inhibition_kinetics.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.2), dpi=300, gridspec_kw={'width_ratios': [1.1, 1.2]})
    
    # Left: Molecular Mechanism
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("Competitive Inhibition Mechanism", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    
    # Enzyme with active site
    e_poly = Polygon([(15, 20), (15, 60), (40, 60), (40, 40), (60, 40), (60, 60), (85, 60), (85, 20)],
                     closed=True, facecolor="#e8f0fe", edgecolor=NAVY, lw=1.6)
    ax1.add_patch(e_poly)
    ax1.text(50, 26, "Enzyme", fontsize=7.5, fontweight='bold', color=NAVY, ha='center')
    ax1.text(50, 46, "Active Site", fontsize=6.2, color=DARK_GREY, ha='center')

    # Substrate
    s_poly = Polygon([(22, 70), (22, 85), (38, 85), (38, 70)], closed=True, facecolor="#e6f4ea", edgecolor="#1a8754", lw=1.4)
    ax1.add_patch(s_poly)
    ax1.text(30, 77.5, "Substrate\n(Succinate)", fontsize=5.8, fontweight='bold', color="#1a8754", ha='center', va='center')

    # Competitive Inhibitor (structurally similar)
    i_poly = Polygon([(62, 70), (62, 85), (78, 85), (78, 70)], closed=True, facecolor="#feeceb", edgecolor=CRIMSON, lw=1.4)
    ax1.add_patch(i_poly)
    ax1.text(70, 77.5, "Inhibitor\n(Malonate)", fontsize=5.8, fontweight='bold', color=CRIMSON, ha='center', va='center')

    ax1.annotate("Competes directly\nfor active site", xy=(50, 42), xytext=(50, 62),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.2, fontweight='bold', color=CRIMSON, ha='center')

    ax1.text(50, 8, "• Reversible binding\n• Overcome by high [Substrate]", fontsize=6.2, color=DARK_GREY, ha='center')

    # Right: Kinetics Curve
    s = np.linspace(0, 50, 200)
    vmax = 100
    km_normal = 5.0
    km_inhibited = 16.0
    
    v_norm = vmax * s / (km_normal + s)
    v_inhib = vmax * s / (km_inhibited + s)
    
    ax2.plot(s, v_norm, color=NAVY, linewidth=2.0, label="Without inhibitor")
    ax2.plot(s, v_inhib, color=CRIMSON, linewidth=2.0, linestyle='--', label="With competitive inhibitor")
    
    # Asymptote
    ax2.plot([0, 50], [vmax, vmax], 'k:', lw=1.0)
    ax2.text(25, 102, "Same Vmax reached at high [S]", fontsize=6.5, fontweight='bold', color=NAVY, ha='center')

    ax2.annotate("Increased Km\n(apparent affinity lowered)", xy=(16, 50), xytext=(22, 32),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=CRIMSON)

    ax2.set_xlim(0, 52)
    ax2.set_ylim(0, 115)
    ax2.set_xlabel("[S] / mmol dm⁻³", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax2.set_ylabel("Rate (V) / AU", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax2.set_title("Competitive Kinetics", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc="lower right", fontsize=6.5, framealpha=0.9)
    ax2.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.11: NON-COMPETITIVE (ALLOSTERIC) INHIBITION
# ==============================================================================
def generate_fig3_11(filename="fig3_11_non_competitive_allosteric.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.2), dpi=300, gridspec_kw={'width_ratios': [1.1, 1.2]})
    
    # Left: Mechanism
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("Non-Competitive Allosteric Mechanism", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    
    # Enzyme with active site and allosteric site
    e_poly = Polygon([(15, 20), (15, 55), (35, 55), (45, 42), (55, 55), (85, 55), (85, 35), (92, 35), (92, 25), (85, 25), (85, 20)],
                     closed=True, facecolor="#e8f0fe", edgecolor=NAVY, lw=1.6)
    ax1.add_patch(e_poly)
    ax1.text(45, 25, "Enzyme", fontsize=7.5, fontweight='bold', color=NAVY, ha='center')
    ax1.text(45, 47, "Altered Active Site\n(Catalysis blocked)", fontsize=5.8, color=CRIMSON, ha='center')

    # Allosteric inhibitor
    ax1.add_patch(Rectangle((89, 26), 9, 8, facecolor="#feeceb", edgecolor=CRIMSON, lw=1.4))
    ax1.annotate("Allosteric\nInhibitor", xy=(93, 30), xytext=(70, 7),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.2, fontweight='bold', color=CRIMSON)

    # Substrate
    s_poly = Polygon([(38, 70), (38, 85), (52, 85), (52, 70)], closed=True, facecolor="#e6f4ea", edgecolor="#1a8754", lw=1.4)
    ax1.add_patch(s_poly)
    ax1.text(45, 77.5, "Substrate", fontsize=6.2, fontweight='bold', color="#1a8754", ha='center', va='center')

    ax1.text(50, 8, "• Binds to allosteric site (not active site)\n• Cannot be overcome by increasing [S]",
             fontsize=6.2, color=DARK_GREY, ha='center')

    # Right: Kinetics Curve
    s = np.linspace(0, 50, 200)
    vmax_norm = 100
    vmax_inhib = 55
    km = 6.0
    
    v_norm = vmax_norm * s / (km + s)
    v_inhib = vmax_inhib * s / (km + s)
    
    ax2.plot(s, v_norm, color=NAVY, linewidth=2.0, label="Without inhibitor (Vmax = 100)")
    ax2.plot(s, v_inhib, color=CRIMSON, linewidth=2.0, linestyle='--', label="With non-competitive inhibitor (Vmax = 55)")
    
    # Asymptotes
    ax2.plot([0, 50], [vmax_norm, vmax_norm], 'k:', lw=1.0)
    ax2.plot([0, 50], [vmax_inhib, vmax_inhib], 'r:', lw=1.0)

    ax2.annotate("Vmax significantly reduced\nFewer functional catalytic sites", xy=(40, 55), xytext=(15, 75),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=CRIMSON)

    ax2.annotate("Same Km (~6 mM)\nRemaining uninhibited sites\nhave normal affinity", xy=(km, 27.5), xytext=(12, 12),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                 fontsize=6.5, fontweight='bold', color=NAVY)

    ax2.set_xlim(0, 52)
    ax2.set_ylim(0, 115)
    ax2.set_xlabel("[S] / mmol dm⁻³", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax2.set_ylabel("Rate (V) / AU", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax2.set_title("Non-Competitive Kinetics", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc="lower right", fontsize=6.5, framealpha=0.9)
    ax2.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.12: LINEWEAVER-BURK DOUBLE RECIPROCAL PLOT
# ==============================================================================
def generate_fig3_12(filename="fig3_12_lineweaver_burk_double_reciprocal.png"):
    fig, ax = plt.subplots(figsize=(7.6, 4.4), dpi=300)
    
    # Double reciprocal equation: 1/V = (Km/Vmax) * (1/[S]) + (1/Vmax)
    # y-intercept = 1/Vmax, x-intercept = -1/Km
    inv_s = np.linspace(-0.35, 0.6, 200)
    
    # 1. Normal: Vmax = 10, Km = 5 -> y-int = 0.1, x-int = -0.2 (slope = 0.5)
    y_norm = 0.5 * inv_s + 0.1
    ax.plot(inv_s, y_norm, color=NAVY, linewidth=2.2, label="Normal uninhibited")

    # 2. Competitive: Vmax = 10 (same y-int), Km = 10 -> x-int = -0.1 (slope = 1.0)
    y_comp = 1.0 * inv_s + 0.1
    ax.plot(inv_s, y_comp, color=CRIMSON, linewidth=2.0, linestyle='--', label="Competitive (Same 1/Vmax, higher Km)")

    # 3. Non-competitive: Vmax = 5 -> y-int = 0.2, Km = 5 -> x-int = -0.2 (slope = 1.0)
    y_noncomp = 1.0 * inv_s + 0.2
    ax.plot(inv_s, y_noncomp, color="#1a8754", linewidth=2.0, linestyle=':', label="Non-competitive (Higher 1/Vmax, same -1/Km)")

    # Axes crossing at (0, 0)
    ax.axhline(0, color='k', linewidth=1.2)
    ax.axvline(0, color='k', linewidth=1.2)

    # Key Intercept Annotations
    ax.plot(0, 0.1, 'o', color=NAVY, markersize=5)
    ax.annotate("y-intercept = 1 / Vmax", xy=(0, 0.1), xytext=(0.08, 0.05),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                fontsize=6.5, fontweight='bold', color=NAVY)

    ax.plot(-0.2, 0, 's', color=NAVY, markersize=5)
    ax.annotate("x-intercept = -1 / Km", xy=(-0.2, 0), xytext=(-0.34, 0.12),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.0),
                fontsize=6.5, fontweight='bold', color=NAVY)

    ax.set_xlim(-0.38, 0.65)
    ax.set_ylim(-0.05, 0.75)
    ax.set_xlabel("1 / [S] (mmol⁻¹ dm³)", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_ylabel("1 / V (AU⁻¹)", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax.set_title("Lineweaver-Burk Double-Reciprocal Plot Diagnostic Comparison",
                 fontsize=8.5, fontweight='bold', color=NAVY, pad=8)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc="upper left", fontsize=6.8, framealpha=0.9)
    ax.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.13: IMMOBILISED ENZYMES IN ALGINATE & BIOREACTOR
# ==============================================================================
def generate_fig3_13(filename="fig3_13_immobilised_enzymes_alginate.png"):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 4.4), dpi=300, gridspec_kw={'width_ratios': [1.0, 1.3]})
    
    # Left: Alginate bead & packed bed reactor
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)
    ax1.axis('off')
    ax1.set_title("Bioreactor Column with Alginate Beads", fontsize=8.0, fontweight='bold', color=NAVY, pad=4)
    
    # Column glass tube
    ax1.add_patch(Rectangle((30, 20), 40, 60, facecolor="#f8fafc", edgecolor=NAVY, lw=1.6))
    
    # Inflow funnel top
    ax1.plot([20, 30], [92, 80], color=NAVY, lw=1.4)
    ax1.plot([80, 70], [92, 80], color=NAVY, lw=1.4)
    ax1.text(50, 94, "Substrate Inflow\n(e.g. Milk with lactose)", fontsize=6.2, fontweight='bold', color="#2b75d6", ha='center')
    
    # Beads packed in column
    np.random.seed(42)
    for bx in np.linspace(36, 64, 5):
        for by in np.linspace(26, 74, 7):
            jitter_x = bx + np.random.uniform(-2, 2)
            jitter_y = by + np.random.uniform(-2, 2)
            ax1.add_patch(Circle((jitter_x, jitter_y), 3.2, facecolor="#e8f0fe", edgecolor="#2b75d6", lw=1.0))
            # Enzyme dot inside bead
            ax1.plot(jitter_x, jitter_y, 'o', color=CRIMSON, markersize=2)

    # Tap outflow bottom
    ax1.plot([46, 46], [20, 10], color=NAVY, lw=1.4)
    ax1.plot([54, 54], [20, 10], color=NAVY, lw=1.4)
    ax1.text(50, 4, "Product Outflow\n(Glucose + Galactose,\nNo enzyme contamination!)",
             fontsize=6.0, fontweight='bold', color="#1a8754", ha='center')

    # Single bead magnification
    ax1.add_patch(Circle((16, 45), 11, facecolor="#e8f0fe", edgecolor="#2b75d6", lw=1.4))
    for ex, ey in [(13, 48), (19, 44), (14, 40), (18, 50)]:
        ax1.plot(ex, ey, 'o', color=CRIMSON, markersize=3)
    ax1.text(16, 31, "Calcium alginate\ngel bead with\nentrapped lactase", fontsize=5.5, color=DARK_GREY, ha='center')

    # Right: Thermal Stability Curves (Free vs Immobilised)
    temp = np.linspace(20, 80, 150)
    # Free enzyme denatures rapidly above 45 deg
    free_act = np.exp(-((temp - 40)**2) / 120) * 100
    free_act[temp > 40] = 100 * np.exp(-((temp[temp > 40] - 40)**2) / 60)
    
    # Immobilised enzyme has wider optimum and resists denaturation up to 65 deg
    immob_act = np.exp(-((temp - 48)**2) / 280) * 100
    
    ax2.plot(temp, free_act, 'r--', linewidth=2.0, label="Free enzyme in solution (denatures > 45 °C)")
    ax2.plot(temp, immob_act, color="#1a8754", linewidth=2.2, label="Immobilised in alginate (stable up to 65 °C)")
    
    ax2.annotate("Enhanced thermal stability:\nAlginate matrix restricts\nunfolding of tertiary structure",
                 xy=(58, 70), xytext=(35, 25),
                 arrowprops=dict(arrowstyle="->", color="#1a8754", lw=1.0),
                 fontsize=6.5, fontweight='bold', color="#1a8754")

    ax2.set_xlim(20, 80)
    ax2.set_ylim(0, 115)
    ax2.set_xlabel("Operating Temperature / °C", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax2.set_ylabel("Catalytic Activity / %", fontsize=7.8, fontweight='bold', color=DARK_GREY)
    ax2.set_title("Thermal Stability Comparison: Free vs Immobilised", fontsize=8.2, fontweight='bold', color=NAVY, pad=4)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc="lower left", fontsize=6.5, framealpha=0.9)
    ax2.tick_params(labelsize=7)

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

# ==============================================================================
# FIG 3.14: END-PRODUCT FEEDBACK INHIBITION
# ==============================================================================
def generate_fig3_14(filename="fig3_14_end_product_allosteric_feedback.png"):
    fig, ax = plt.subplots(figsize=(8.0, 4.2), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 70)
    ax.axis('off')
    
    ax.text(50, 66, "End-Product Allosteric Feedback Inhibition Pathway",
            fontsize=8.8, fontweight='bold', color=NAVY, ha='center')
    
    # Pathway metabolites
    nodes = [
        ("Initial Substrate\n(L-Threonine)", 14, 45, "#e8f0fe", NAVY),
        ("Intermediate A\n(α-Ketobutyrate)", 36, 45, "#f8fafc", DARK_GREY),
        ("Intermediate B", 56, 45, "#f8fafc", DARK_GREY),
        ("Final End-Product\n(L-Isoleucine)", 84, 45, "#feeceb", CRIMSON)
    ]
    
    for label, x, y, fc, ec in nodes:
        ax.add_patch(FancyBboxPatch((x-10, y-10), 20, 20, boxstyle="round,pad=1,rounding_size=4",
                                     facecolor=fc, edgecolor=ec, lw=1.5))
        ax.text(x, y, label, fontsize=6.5, fontweight='bold', color=ec, ha='center', va='center')

    # Forward reaction arrows with enzyme labels
    ax.annotate("", xy=(25, 45), xytext=(24.5, 45), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.5))
    ax.text(25, 50, "Enzyme 1\n(Threonine deaminase)", fontsize=5.8, fontweight='bold', color=NAVY, ha='center')
    
    ax.annotate("", xy=(46, 45), xytext=(45.5, 45), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.5))
    ax.text(46, 50, "Enzyme 2", fontsize=5.8, color=DARK_GREY, ha='center')

    ax.annotate("", xy=(68, 45), xytext=(67.5, 45), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.5))
    ax.text(70, 50, "Enzymes 3 & 4", fontsize=5.8, color=DARK_GREY, ha='center')

    # Feedback inhibition loop from End Product back to Enzyme 1 allosteric site
    fb_path = [(84, 33), (84, 16), (25, 16), (25, 38)]
    fb_codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
    ax.add_patch(PathPatch(Path(fb_path, fb_codes), facecolor="none", edgecolor=CRIMSON, lw=2.0, linestyle='--'))
    ax.annotate("", xy=(25, 38), xytext=(25, 35), arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=2.0))
    
    ax.text(54.5, 20, "Reversible Allosteric Inhibition\nWhen [Isoleucine] accumulates, it binds to allosteric site of Enzyme 1,\nshutting down entire pathway to conserve cellular resources",
            fontsize=6.2, fontweight='bold', color=CRIMSON, ha='center',
            bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f2", ec=CRIMSON, lw=0.8))

    plt.tight_layout()
    outpath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(outpath, dpi=300)
    plt.close()
    print(f"[OK] Generated {outpath}")

def main():
    print("Generating all 14 Biological Diagrams for Topic 3: Enzymes...")
    generate_fig3_1()
    generate_fig3_2()
    generate_fig3_3()
    generate_fig3_4()
    generate_fig3_5()
    generate_fig3_6()
    generate_fig3_7()
    generate_fig3_8()
    generate_fig3_9()
    generate_fig3_10()
    generate_fig3_11()
    generate_fig3_12()
    generate_fig3_13()
    generate_fig3_14()
    print("All 14 Topic 3 diagrams successfully generated!")

if __name__ == "__main__":
    main()
