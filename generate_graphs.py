"""
Generate publication-quality Cambridge exam graphs and diagrams using Matplotlib.
Matches the visual styling of Mentora Academy (Urwah worksheets).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = r"z:\tests n quizes63\books\psycology\new styl\figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Styling palette
NAVY = "#0b1b36"
DEEP_NAVY = "#132646"
CRIMSON = "#a81717"
GRID_GREY = "#e5e3dc"
BG_COLOR = "#ffffff"
BOX_BG = "#fbfaf8"

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def save_clean_figure(fig, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"[OK] Saved figure: {filepath}")
    return filepath

def generate_atomic_radius_period3():
    elements = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
    radii = [186, 160, 143, 117, 110, 104, 99, 71]

    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=200)
    ax.set_facecolor(BG_COLOR)
    fig.patch.set_facecolor(BG_COLOR)

    ax.plot(elements, radii, color=CRIMSON, marker='o', markersize=6, 
            markerfacecolor=NAVY, markeredgecolor=NAVY, linewidth=2, zorder=4)

    ax.set_title('Atomic Radius Across Period 3', fontsize=12, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlabel('Element (Period 3)', fontsize=10, fontweight='bold', color=NAVY, labelpad=8)
    ax.set_ylabel('Atomic radius / pm', fontsize=10, fontweight='bold', color=NAVY, labelpad=8)

    ax.set_ylim(60, 200)
    ax.grid(True, linestyle='-', color=GRID_GREY, linewidth=0.8, zorder=1)
    
    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_color(NAVY)
        ax.spines[spine].set_linewidth(1.0)

    ax.tick_params(colors=NAVY, labelsize=9)
    return save_clean_figure(fig, "atomic_radius_period3.png")

def generate_mass_spectrum():
    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=200)
    ax.set_facecolor(BG_COLOR)
    fig.patch.set_facecolor(BG_COLOR)

    mz_peaks = [24, 25, 26]
    abundances = [79.0, 10.0, 11.0]

    for mz, ab in zip(mz_peaks, abundances):
        ax.plot([mz, mz], [0, ab], color=CRIMSON, linewidth=3.5, zorder=3)
        ax.scatter([mz], [ab], color=NAVY, s=25, zorder=4)
        ax.text(mz, ab + 2.5, f'{ab:.1f}%', ha='center', va='bottom', fontsize=8.5, fontweight='bold', color=NAVY)

    ax.set_title('Mass Spectrum of Element Q', fontsize=12, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlabel('m / z', fontsize=10, fontweight='bold', color=NAVY, labelpad=8)
    ax.set_ylabel('Relative abundance (%)', fontsize=10, fontweight='bold', color=NAVY, labelpad=8)

    ax.set_xlim(22, 28)
    ax.set_ylim(0, 95)
    ax.grid(True, linestyle='--', color=GRID_GREY, linewidth=0.8, zorder=1)

    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_color(NAVY)
        ax.spines[spine].set_linewidth(1.0)

    ax.tick_params(colors=NAVY, labelsize=9)
    return save_clean_figure(fig, "mass_spectrum.png")

def generate_subshell_energy():
    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=200)
    ax.set_facecolor(BG_COLOR)
    fig.patch.set_facecolor(BG_COLOR)

    # Sub-shell levels (name, energy_y, list of x positions)
    levels = [
        ('1s', 1.0, [0.35]),
        ('2s', 2.2, [0.35]),
        ('2p', 2.8, [0.55, 0.65, 0.75]),
        ('3s', 4.0, [0.35]),
        ('3p', 4.6, [0.55, 0.65, 0.75]),
        ('4s', 5.6, [0.35]),
        ('3d', 6.2, [0.45, 0.53, 0.61, 0.69, 0.77]),
    ]

    for label, y, xs in levels:
        for x in xs:
            ax.plot([x - 0.035, x + 0.035], [y, y], color=CRIMSON, linewidth=2.5)
        ax.text(xs[0] - 0.07, y, label, ha='right', va='center', fontsize=9, fontweight='bold', color=NAVY)

    ax.annotate('', xy=(0.15, 6.8), xytext=(0.15, 0.5),
                arrowprops=dict(facecolor=NAVY, edgecolor=NAVY, width=1.5, headwidth=7))
    ax.text(0.12, 3.65, 'Increasing Energy', rotation=90, ha='center', va='center', fontsize=9, fontweight='bold', color=NAVY)

    ax.set_xlim(0.05, 0.9)
    ax.set_ylim(0.2, 7.2)
    ax.set_title('Relative Energies of Atomic Orbitals', fontsize=12, fontweight='bold', color=NAVY, pad=12)
    ax.axis('off')

    return save_clean_figure(fig, "subshell_energy.png")

def generate_period3_first_ie():
    elements = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
    ie_values = [496, 738, 578, 789, 1012, 1000, 1251, 1521]

    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=200)
    ax.set_facecolor(BG_COLOR)
    fig.patch.set_facecolor(BG_COLOR)

    ax.plot(elements, ie_values, color=CRIMSON, marker='s', markersize=6, 
            markerfacecolor=NAVY, markeredgecolor=NAVY, linewidth=2, zorder=4)

    ax.set_title('First Ionisation Energy Across Period 3', fontsize=12, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlabel('Element (Period 3)', fontsize=10, fontweight='bold', color=NAVY, labelpad=8)
    ax.set_ylabel('First ionisation energy / kJ mol⁻¹', fontsize=10, fontweight='bold', color=NAVY, labelpad=8)

    ax.set_ylim(400, 1650)
    ax.grid(True, linestyle='-', color=GRID_GREY, linewidth=0.8, zorder=1)

    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_color(NAVY)
        ax.spines[spine].set_linewidth(1.0)

    ax.tick_params(colors=NAVY, labelsize=9)
    return save_clean_figure(fig, "period3_first_ie.png")

def generate_successive_ie():
    electrons = list(range(1, 16))
    # Phosphorus successive IE: 1012, 1907, 2914, 4964, 6274, 21267, 25431, ...
    ie_raw = [1012, 1907, 2914, 4964, 6274, 21267, 25431, 29872, 35905, 40950, 46261, 54142, 62051, 271600, 296100]
    log_ie = np.log10(ie_raw)

    fig, ax = plt.subplots(figsize=(6.5, 3.8), dpi=200)
    ax.set_facecolor(BG_COLOR)
    fig.patch.set_facecolor(BG_COLOR)

    ax.plot(electrons, log_ie, color=CRIMSON, marker='o', markersize=5, 
            markerfacecolor=NAVY, markeredgecolor=NAVY, linewidth=1.8, zorder=4)

    ax.set_title('Successive Ionisation Energies of Element X', fontsize=12, fontweight='bold', color=NAVY, pad=12)
    ax.set_xlabel('Number of electrons removed', fontsize=10, fontweight='bold', color=NAVY, labelpad=8)
    ax.set_ylabel('log₁₀ (Ionisation energy / kJ mol⁻¹)', fontsize=10, fontweight='bold', color=NAVY, labelpad=8)

    ax.set_xticks(electrons)
    ax.set_ylim(2.5, 5.8)
    ax.grid(True, linestyle='--', color=GRID_GREY, linewidth=0.8, zorder=1)

    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_color(NAVY)
        ax.spines[spine].set_linewidth(1.0)

    ax.tick_params(colors=NAVY, labelsize=8.5)
    return save_clean_figure(fig, "successive_ie.png")

if __name__ == "__main__":
    generate_atomic_radius_period3()
    generate_mass_spectrum()
    generate_subshell_energy()
    generate_period3_first_ie()
    generate_successive_ie()
    print("All figures generated successfully.")
