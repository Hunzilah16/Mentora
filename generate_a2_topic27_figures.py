"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for Topic 27: Group 2
Candidate: Urwah | Mentora Academy
"""
import os
import matplotlib.pyplot as plt
import numpy as np

fig_dir = r"z:\tests n quizes63\books\psycology\new styl\figures"
os.makedirs(fig_dir, exist_ok=True)

plt.rcParams.update({
    'font.sans-serif': 'Arial',
    'font.family': 'sans-serif',
    'figure.autolayout': True,
    'axes.edgecolor': '#0b1b36',
    'axes.linewidth': 1.0,
})

# -----------------------------------------------------------------------------
# Figure 1: Thermal Decomposition Temperature vs Cationic Radius (Carbonates & Nitrates)
# -----------------------------------------------------------------------------
def create_thermal_stability_graph():
    fig, ax = plt.subplots(figsize=(6.0, 3.2), dpi=220)

    metals = ['Mg', 'Ca', 'Sr', 'Ba']
    radii = [0.065, 0.099, 0.113, 0.135] # nm (cation radius)
    t_carb = [540, 900, 1290, 1360] # °C (decomposition temp of carbonates)
    t_nitr = [350, 500, 570, 600]   # °C (decomposition temp of nitrates)

    ax.plot(radii, t_carb, 'o-', color='#a81717', lw=2.0, markersize=6, label=r'$\mathrm{Carbonates\ (MCO_3)}$')
    ax.plot(radii, t_nitr, 's--', color='#1565c0', lw=2.0, markersize=6, label=r'$\mathrm{Nitrates\ (M(NO_3)_2)}$')

    for i, m in enumerate(metals):
        ax.annotate(f"{m}CO3\n({t_carb[i]} °C)", (radii[i], t_carb[i]), textcoords="offset points", xytext=(-10, 8),
                    fontsize=6.8, fontweight='bold', color='#a81717')
        ax.annotate(f"{m}(NO3)2\n({t_nitr[i]} °C)", (radii[i], t_nitr[i]), textcoords="offset points", xytext=(-12, -18),
                    fontsize=6.8, fontweight='bold', color='#1565c0')

    ax.set_xlabel(r'Cationic Radius of $\mathrm{M^{2+}}$ / $\mathrm{nm}$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'Decomposition Temperature / $\mathrm{^\circ C}$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Thermal Stability Trend of Group 2 Carbonates and Nitrates down the Group', fontsize=8.5, fontweight='bold', color='#0b1b36')

    ax.set_xlim(0.055, 0.145)
    ax.set_ylim(250, 1500)
    ax.grid(True, linestyle=':', alpha=0.5, color='#b0aca4')
    ax.legend(frameon=True, facecolor='#f8f9fa', edgecolor='#dcd8d0', fontsize=7.2, loc='upper left')

    out_file = os.path.join(fig_dir, "a2_t27_thermal_stability_trend.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 2: Enthalpy of Solution Analysis: Sulfates vs Hydroxides
# -----------------------------------------------------------------------------
def create_solubility_enthalpy_bar():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.0), dpi=220)

    metals = ['Mg', 'Ca', 'Sr', 'Ba']
    # Group 2 Sulfates: Delta H sol becomes more positive (less soluble down group)
    dh_sol_sulf = [-91, -18, -8, +19] # kJ/mol
    colors_sulf = ['#2e7d32' if x < 0 else '#c2185b' for x in dh_sol_sulf]

    ax1.bar(metals, dh_sol_sulf, color=colors_sulf, width=0.5, edgecolor='#0b1b36', lw=0.8)
    ax1.axhline(0, color='#0b1b36', lw=0.8)
    ax1.set_ylabel(r'$\Delta H_{\mathrm{sol}}^\circ\ /\ \mathrm{kJ\ mol^{-1}}$', fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax1.set_title(r'$\mathbf{Group\ 2\ Sulfates\ (MSO_4)}$' '\n' r'Solubility decreases down group', fontsize=7.5, color='#0b1b36')
    ax1.grid(True, linestyle=':', alpha=0.4, axis='y')
    for i, v in enumerate(dh_sol_sulf):
        y_pos = v + 4 if v >= 0 else v - 12
        ax1.text(i, y_pos, f"{v:+d}", ha='center', fontsize=6.8, fontweight='bold')

    # Group 2 Hydroxides: Delta H sol becomes more negative (more soluble down group)
    dh_sol_hydr = [+3, -17, -46, -103] # kJ/mol
    colors_hydr = ['#2e7d32' if x < 0 else '#c2185b' for x in dh_sol_hydr]

    ax2.bar(metals, dh_sol_hydr, color=colors_hydr, width=0.5, edgecolor='#0b1b36', lw=0.8)
    ax2.axhline(0, color='#0b1b36', lw=0.8)
    ax2.set_ylabel(r'$\Delta H_{\mathrm{sol}}^\circ\ /\ \mathrm{kJ\ mol^{-1}}$', fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax2.set_title(r'$\mathbf{Group\ 2\ Hydroxides\ (M(OH)_2)}$' '\n' r'Solubility increases down group', fontsize=7.5, color='#0b1b36')
    ax2.grid(True, linestyle=':', alpha=0.4, axis='y')
    for i, v in enumerate(dh_sol_hydr):
        y_pos = v + 4 if v >= 0 else v - 12
        ax2.text(i, y_pos, f"{v:+d}", ha='center', fontsize=6.8, fontweight='bold')

    out_file = os.path.join(fig_dir, "a2_t27_solubility_enthalpy_trends.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 3: Anion Polarisation Diagram (M2+ distorting CO3 2-)
# -----------------------------------------------------------------------------
def create_anion_polarisation_scheme():
    fig, ax = plt.subplots(figsize=(6.0, 2.8), dpi=220)

    # Left: Mg2+ (small, high charge density) strongly polarizing CO3 2-
    # Draw Mg2+
    circle_mg = plt.Circle((2.0, 2.0), 0.4, color='#1565c0', fill=True, ec='#0b1b36', lw=1.2)
    ax.add_patch(circle_mg)
    ax.text(2.0, 2.0, r'$\mathbf{Mg^{2+}}$', color='white', ha='center', va='center', fontsize=7.5, fontweight='bold')
    ax.text(2.0, 1.2, r'Small radius' '\n' r'High charge density' '\n' r'$\mathbf{Strong\ polarising}$', ha='center', fontsize=6.5, color='#0b1b36')

    # Draw distorted carbonate cloud (ellipse)
    ellipse1 = plt.matplotlib.patches.Ellipse((3.5, 2.0), 1.5, 0.9, angle=-10, color='#ffcdd2', fill=True, ec='#c2185b', lw=1.2)
    ax.add_patch(ellipse1)
    ax.text(3.5, 2.0, r'$\mathbf{CO_3^{2-}}$' '\n(Distorted C-O bond)', ha='center', va='center', fontsize=6.5, color='#c2185b', fontweight='bold')

    # Right: Ba2+ (large, low charge density) weakly polarizing CO3 2-
    circle_ba = plt.Circle((6.5, 2.0), 0.7, color='#1565c0', fill=True, ec='#0b1b36', lw=1.2)
    ax.add_patch(circle_ba)
    ax.text(6.5, 2.0, r'$\mathbf{Ba^{2+}}$', color='white', ha='center', va='center', fontsize=8.0, fontweight='bold')
    ax.text(6.5, 1.0, r'Large radius' '\n' r'Low charge density' '\n' r'$\mathbf{Weak\ polarising}$', ha='center', fontsize=6.5, color='#0b1b36')

    # Undistorted carbonate (circle)
    circle_carb = plt.Circle((8.2, 2.0), 0.6, color='#ffcdd2', fill=True, ec='#c2185b', lw=1.2)
    ax.add_patch(circle_carb)
    ax.text(8.2, 2.0, r'$\mathbf{CO_3^{2-}}$' '\n(Spherical)', ha='center', va='center', fontsize=6.5, color='#c2185b', fontweight='bold')

    ax.set_xlim(0.5, 9.5)
    ax.set_ylim(0.4, 3.2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'Polarisation of Carbonate Anion Electron Cloud by Group 2 Cations', fontsize=8.5, fontweight='bold', color='#0b1b36')

    out_file = os.path.join(fig_dir, "a2_t27_polarisation_mechanism.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_thermal_stability_graph()
    create_solubility_enthalpy_bar()
    create_anion_polarisation_scheme()
    print("All Topic 27 figures successfully generated.")
