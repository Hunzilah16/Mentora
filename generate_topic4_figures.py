"""
Generate high-resolution figures for Topic 4: States of Matter.
"""
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs(r"z:\tests n quizes63\books\psycology\new styl\figures", exist_ok=True)
fig_dir = r"z:\tests n quizes63\books\psycology\new styl\figures"

plt.rcParams.update({
    'font.sans-serif': 'Arial',
    'font.family': 'sans-serif',
    'figure.autolayout': True,
    'axes.edgecolor': '#2a3b5c',
    'axes.linewidth': 1.2,
})

# -------------------------------------------------------------
# Figure 1: Real vs Ideal Gas Deviations (pV/nRT vs p)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.4), dpi=200)

p = np.linspace(0, 1000, 400)

# Ideal gas
ax.axhline(1.0, color='#0b1b36', linestyle='--', linewidth=1.8, label='Ideal Gas (pV/nRT = 1.0)')

# Real gases
# H2 (almost purely repulsive effect dominating due to very small size and weak London forces)
z_h2 = 1.0 + 0.00045 * p
ax.plot(p, z_h2, color='#1e88e5', linewidth=2.0, label=r'$\mathrm{H_2}$ (298 K)')

# N2 (dip due to attraction, then rise due to volume)
z_n2 = 1.0 - 0.0006 * p * np.exp(-p / 250) + 0.00055 * p
ax.plot(p, z_n2, color='#2e7d32', linewidth=2.0, label=r'$\mathrm{N_2}$ (298 K)')

# CO2 (stronger dip due to greater polarisability / attractions)
z_co2 = 1.0 - 0.0022 * p * np.exp(-p / 200) + 0.0007 * p
ax.plot(p, z_co2, color='#a81717', linewidth=2.0, label=r'$\mathrm{CO_2}$ (298 K)')

# Low T vs High T for N2
z_n2_lowT = 1.0 - 0.0016 * p * np.exp(-p / 220) + 0.00065 * p
ax.plot(p, z_n2_lowT, color='#e65100', linewidth=1.8, linestyle=':', label=r'$\mathrm{N_2}$ (200 K, low T)')

ax.set_title(r'Deviation of Real Gases from Ideal Behaviour: $\frac{pV}{nRT}$ vs Pressure', fontsize=11, fontweight='bold', color='#0b1b36', pad=10)
ax.set_xlabel('Pressure / atm', fontsize=9.5, fontweight='bold', color='#0b1b36')
ax.set_ylabel(r'Compressibility Factor, $Z = \frac{pV}{nRT}$', fontsize=9.5, fontweight='bold', color='#0b1b36')
ax.set_xlim(0, 1000)
ax.set_ylim(0.4, 1.8)
ax.grid(True, linestyle=':', alpha=0.6, color='#99aab5')

# Annotations
ax.annotate('Attractions dominate\n(negative deviation)', xy=(180, 0.68), xytext=(220, 0.48),
            arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.2),
            fontsize=8, color='#a81717', fontweight='semibold')
ax.annotate('Molecular volume dominates\n(positive deviation)', xy=(750, 1.45), xytext=(550, 1.6),
            arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.2),
            fontsize=8, color='#0b1b36', fontweight='semibold')

ax.legend(frameon=True, facecolor='#f8f9fa', edgecolor='#b0aca4', fontsize=8, loc='upper left')
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'real_vs_ideal_gas.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 2: Gas Syringe Apparatus for Volatile Liquid Mr
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.4), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Water/steam oven box
rect_oven = plt.Rectangle((1.5, 1.5), 6.5, 3.0, facecolor='#e3f2fd', edgecolor='#0b1b36', linewidth=1.5)
ax.add_patch(rect_oven)
ax.text(4.75, 4.2, 'Steam Jacket / Temperature-Controlled Oven', ha='center', fontsize=9, fontweight='bold', color='#0b1b36')

# Gas syringe body inside
rect_syr = plt.Rectangle((2.5, 2.3), 4.5, 1.2, facecolor='#ffffff', edgecolor='#333333', linewidth=1.2)
ax.add_patch(rect_syr)
# Syringe graduations
for gx in np.linspace(2.8, 6.0, 9):
    ax.plot([gx, gx], [2.3, 2.6], color='#555555', lw=1)
ax.text(4.4, 2.4, r'Graduated Syringe ($100\ \mathrm{cm^3}$)', ha='center', fontsize=7.5, color='#333333')

# Syringe plunger
plunger_shaft = plt.Rectangle((5.5, 2.7), 2.8, 0.4, facecolor='#b0bec5', edgecolor='#333333', linewidth=1)
plunger_head = plt.Rectangle((5.3, 2.4), 0.2, 1.0, facecolor='#455a64', edgecolor='#333333', linewidth=1)
ax.add_patch(plunger_shaft)
ax.add_patch(plunger_head)

# Capillary / nozzle & self-sealing cap
ax.plot([2.5, 1.8], [2.9, 2.9], color='#333333', lw=2)
cap = plt.Rectangle((1.5, 2.7), 0.3, 0.4, facecolor='#d32f2f', edgecolor='#333333', lw=1)
ax.add_patch(cap)
ax.text(1.65, 2.3, 'Self-sealing\nrubber cap', ha='center', fontsize=7.5, color='#d32f2f', fontweight='semibold')

# Hypodermic syringe injection
ax.annotate('Volatile liquid injected\nvia micro-syringe', xy=(1.8, 2.9), xytext=(0.5, 4.0),
            arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.3),
            fontsize=8, color='#a81717', fontweight='bold')

# Thermometer
ax.plot([7.2, 7.2], [1.8, 4.8], color='#c62828', lw=2.5)
ax.text(7.4, 4.5, 'Thermometer\n(measures T)', fontsize=7.5, color='#c62828', va='center')

# Pressure gauge
ax.annotate('Atmospheric pressure (p)\nmeasured by barometer', xy=(4.5, 1.5), xytext=(4.5, 0.6),
            arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.2),
            ha='center', fontsize=8, color='#0b1b36', fontweight='bold')

ax.set_title(r'Experimental Determination of $M_\mathrm{r}$ Using a Gas Syringe', fontsize=10.5, fontweight='bold', color='#0b1b36')
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'gas_syringe_apparatus.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 3: Carbon Allotropes & Giant Structures
# -------------------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(7.2, 2.8), dpi=200)

# Diamond
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.axis('off')
ax1.set_title('Diamond\n(Giant Covalent)', fontsize=8.5, fontweight='bold', color='#0b1b36')
pts_dia = [(0, 0), (-1.2, -1.2), (1.2, -1.2), (-0.6, 1.2), (0.6, 1.2)]
for p in pts_dia[1:]:
    ax1.plot([0, p[0]], [0, p[1]], color='#222222', lw=2)
for p in pts_dia:
    ax1.scatter(p[0], p[1], s=140, color='#1565c0', edgecolors='#0b1b36', zorder=5)
ax1.text(0, -1.8, r'$\mathrm{sp^3}$ tetrahedral (109.5°)' '\nNo delocalised e⁻\nHard, insulator', ha='center', fontsize=7, color='#333333')

# Graphite
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.axis('off')
ax2.set_title('Graphite\n(Giant Layered)', fontsize=8.5, fontweight='bold', color='#0b1b36')
# Layer 1
ax2.plot([-1.5, -0.5, 0.5, 1.5], [0.8, 1.1, 0.8, 1.1], color='#222222', lw=2)
ax2.scatter([-1.5, -0.5, 0.5, 1.5], [0.8, 1.1, 0.8, 1.1], s=90, color='#2e7d32', edgecolors='#0b1b36', zorder=5)
# Layer 2
ax2.plot([-1.5, -0.5, 0.5, 1.5], [-0.5, -0.2, -0.5, -0.2], color='#222222', lw=2)
ax2.scatter([-1.5, -0.5, 0.5, 1.5], [-0.5, -0.2, -0.5, -0.2], s=90, color='#2e7d32', edgecolors='#0b1b36', zorder=5)
# London forces between layers
for x in [-1.0, 0.0, 1.0]:
    ax2.plot([x, x], [0.7, -0.1], color='#a81717', linestyle=':', lw=1.5)
ax2.text(0, -1.8, r'$\mathrm{sp^2}$ hexagonal layers (120°)' '\nDelocalised $\pi$ e⁻ (conducts)\nWeak dispersion forces', ha='center', fontsize=7, color='#333333')

# Fullerene C60
ax3.set_xlim(-2, 2)
ax3.set_ylim(-2, 2)
ax3.axis('off')
ax3.set_title(r'Fullerene $\mathrm{C_{60}}$' '\n(Simple Molecular)', fontsize=8.5, fontweight='bold', color='#0b1b36')
circle = plt.Circle((0, 0.2), 1.0, facecolor='#fff3e0', edgecolor='#e65100', linewidth=2, linestyle='--')
ax3.add_patch(circle)
# Hexagonal ring on front
theta = np.linspace(0, 2*np.pi, 7)
hx = 0.5 * np.cos(theta)
hy = 0.2 + 0.5 * np.sin(theta)
ax3.plot(hx, hy, color='#d84315', lw=1.8)
ax3.scatter(hx, hy, s=40, color='#e65100', zorder=5)
ax3.text(0, -1.8, 'Discrete cage of 60 C atoms\nWeak London forces between cages\nSoluble in organic solvents', ha='center', fontsize=7, color='#333333')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'carbon_allotropes_structure.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 4: Ice Open Hexagonal Lattice vs Liquid Water
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.0, 3.2), dpi=200)
ax.set_xlim(-3, 3)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')

# Hexagonal arrangement of oxygen atoms
r = 1.6
angles = np.linspace(np.pi/6, 2*np.pi + np.pi/6, 7)
ox = r * np.cos(angles)
oy = r * np.sin(angles)

# Plot covalent and hydrogen bonds
for i in range(6):
    # Covalent bond (thick solid)
    mx = 0.6 * ox[i] + 0.4 * ox[i+1]
    my = 0.6 * oy[i] + 0.4 * oy[i+1]
    ax.plot([ox[i], mx], [oy[i], my], color='#0b1b36', lw=2.5)
    # Hydrogen bond (dashed)
    ax.plot([mx, ox[i+1]], [my, oy[i+1]], color='#c62828', linestyle='--', lw=2.0)
    # Hydrogen atom
    ax.scatter(mx, my, s=70, color='#90caf9', edgecolors='#0b1b36', zorder=6)

# Oxygen atoms
ax.scatter(ox[:6], oy[:6], s=220, color='#e53935', edgecolors='#0b1b36', zorder=7)
for i in range(6):
    ax.text(ox[i], oy[i], 'O', ha='center', va='center', color='white', fontweight='bold', fontsize=9, zorder=8)

# Central cavity
ax.text(0, 0, 'Open cavity\n(causes lower\ndensity of ice)', ha='center', va='center', fontsize=8, fontweight='bold', color='#1565c0')

ax.set_title('Open Hexagonal Hydrogen-Bonded Lattice of Ice (0 °C)', fontsize=10.5, fontweight='bold', color='#0b1b36', pad=10)
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'ice_lattice_structure.png'), dpi=200)
plt.close(fig)

print("Generated Topic 4 figures successfully!")
