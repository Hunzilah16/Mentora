"""
Generate high-resolution figures for Topic 8: Reaction Kinetics.
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
# Figure 1: Maxwell-Boltzmann Distribution at T1 and T2
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.4), dpi=200)

E = np.linspace(0, 10, 500)

# Distribution function: P(E) ~ E * exp(-E / kT)
# T1 (lower T, e.g. 300 K): kT = 1.5
p_t1 = 1.8 * (E / 1.5**2) * np.exp(-E / 1.5)
# T2 (higher T, e.g. 310 K): kT = 2.2
p_t2 = 1.8 * (E / 2.2**2) * np.exp(-E / 2.2)

ax.plot(E, p_t1, color='#1565c0', lw=2.2, label=r'Temperature $T_1$ (lower T)')
ax.plot(E, p_t2, color='#a81717', lw=2.2, label=r'Temperature $T_2$ ($T_2 > T_1$)')

# Activation Energy Ea at E = 6.0
ea = 6.0
ax.axvline(ea, color='#212121', linestyle='--', lw=1.8)
ax.text(ea + 0.1, 0.45, r'Activation Energy, $E_\mathrm{a}$', fontsize=8.5, fontweight='bold', color='#212121')

# Shading for T1 (E >= Ea)
mask_t1 = E >= ea
ax.fill_between(E[mask_t1], 0, p_t1[mask_t1], color='#1565c0', alpha=0.35, hatch='//', label=r'Particles with $E \geq E_\mathrm{a}$ at $T_1$')

# Shading for T2 (E >= Ea)
ax.fill_between(E[mask_t1], p_t1[mask_t1], p_t2[mask_t1], color='#a81717', alpha=0.35, hatch='\\\\', label=r'Additional particles with $E \geq E_\mathrm{a}$ at $T_2$')

# Peak shift annotation
ax.annotate('Peak shifts down\nand to the right', xy=(2.2, 0.30), xytext=(3.5, 0.38),
            arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.2),
            fontsize=8, color='#a81717', fontweight='semibold')

# Origin annotation
ax.scatter(0, 0, color='#212121', s=30, zorder=5)
ax.text(0.1, 0.02, 'Starts at (0,0)\nNo particles have zero energy', fontsize=7.5, color='#424242')

ax.set_title(r'Maxwell-Boltzmann Energy Distribution at Two Temperatures ($T_2 > T_1$)', fontsize=10, fontweight='bold', color='#0b1b36', pad=10)
ax.set_xlabel('Molecular Kinetic Energy, E', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_ylabel('Fraction / Number of Molecules', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_xlim(0, 10)
ax.set_ylim(0, 0.5)
ax.grid(True, linestyle=':', alpha=0.6, color='#99aab5')
ax.legend(frameon=True, facecolor='#f8f9fa', fontsize=7.5, loc='upper right')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'maxwell_boltzmann_two_temperatures.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 2: Maxwell-Boltzmann Distribution with Catalyst
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=200)

ax.plot(E, p_t1, color='#0b1b36', lw=2.2, label='Maxwell-Boltzmann Distribution')

# Uncatalysed Ea = 6.5
ea_uncat = 6.5
ax.axvline(ea_uncat, color='#a81717', linestyle='--', lw=1.8)
ax.text(ea_uncat + 0.1, 0.38, r'Uncatalysed $E_\mathrm{a}$', fontsize=8, fontweight='bold', color='#a81717')

# Catalysed Ea = 4.2
ea_cat = 4.2
ax.axvline(ea_cat, color='#2e7d32', linestyle='--', lw=1.8)
ax.text(ea_cat - 1.8, 0.38, r'Catalysed $E_\mathrm{cat}$', fontsize=8, fontweight='bold', color='#2e7d32')

# Shading for uncatalysed
mask_uncat = E >= ea_uncat
ax.fill_between(E[mask_uncat], 0, p_t1[mask_uncat], color='#a81717', alpha=0.4, label=r'Particles with $E \geq E_\mathrm{a}$ (uncatalysed)')

# Additional shading with catalyst
mask_cat = (E >= ea_cat) & (E <= ea_uncat)
ax.fill_between(E[mask_cat], 0, p_t1[mask_cat], color='#2e7d32', alpha=0.35, hatch='//', label=r'Extra particles with $E \geq E_\mathrm{cat}$ (catalysed)')

ax.set_title('Effect of a Catalyst on the Maxwell-Boltzmann Distribution', fontsize=10, fontweight='bold', color='#0b1b36', pad=10)
ax.set_xlabel('Molecular Kinetic Energy, E', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_ylabel('Fraction / Number of Molecules', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_xlim(0, 10)
ax.set_ylim(0, 0.5)
ax.grid(True, linestyle=':', alpha=0.6, color='#99aab5')
ax.legend(frameon=True, facecolor='#f8f9fa', fontsize=7.5, loc='upper right')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'boltzmann_distribution_catalyst.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 3: Concentration-Time Curve & Tangents (Initial & Instantaneous Rates)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=200)

t = np.linspace(0, 10, 200)
conc = 1.0 * np.exp(-0.4 * t)

ax.plot(t, conc, color='#0b1b36', lw=2.5, label='[Reactant] vs time curve')

# Tangent at t = 0 (Initial Rate)
# slope = -0.4 * 1.0 = -0.4
t_tan0 = np.linspace(0, 2.5, 50)
conc_tan0 = 1.0 - 0.4 * t_tan0
ax.plot(t_tan0, conc_tan0, '--', color='#a81717', lw=1.8, label=r'Tangent at $t = 0$ (Initial Rate)')

# Tangent at t = 3 (Instantaneous Rate)
# conc(3) = exp(-1.2) = 0.301, slope = -0.4 * 0.301 = -0.120
t_tan3 = np.linspace(1.0, 5.0, 50)
conc_tan3 = 0.301 - 0.120 * (t_tan3 - 3.0)
ax.plot(t_tan3, conc_tan3, '--', color='#1565c0', lw=1.8, label=r'Tangent at $t = 3\ \mathrm{min}$ (Instantaneous Rate)')
ax.plot(3.0, 0.301, 'o', color='#1565c0', markersize=6)

ax.annotate(r'Initial Rate = $-\mathrm{gradient\ at}\ t=0$', xy=(0.8, 0.68), xytext=(2.0, 0.85),
            arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.2),
            fontsize=8, color='#a81717', fontweight='bold')

ax.annotate(r'Rate at $t_1$ = $-\mathrm{gradient\ at}\ t_1$', xy=(3.0, 0.301), xytext=(4.5, 0.45),
            arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.2),
            fontsize=8, color='#1565c0', fontweight='bold')

ax.set_title(r'Determination of Reaction Rates from Concentration-Time Curves', fontsize=10, fontweight='bold', color='#0b1b36', pad=10)
ax.set_xlabel('Time / min', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_ylabel(r'Concentration / $\mathrm{mol\ dm^{-3}}$', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_xlim(-0.2, 10)
ax.set_ylim(0, 1.1)
ax.grid(True, linestyle=':', alpha=0.6, color='#99aab5')
ax.legend(frameon=True, facecolor='#f8f9fa', fontsize=7.5, loc='upper right')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'rate_concentration_tangents.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 4: Heterogeneous Catalysis Mechanism on Solid Surface
# -------------------------------------------------------------
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(7.2, 2.5), dpi=200)

titles = ['1. Diffusion &\nAdsorption', '2. Bond Weakening\n& Activation', '3. Reaction Between\nAdsorbed Species', '4. Desorption of\nProduct Molecules']
axes = [ax1, ax2, ax3, ax4]

for i, ax in enumerate(axes):
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.axis('off')
    ax.set_title(titles[i], fontsize=7.5, fontweight='bold', color='#0b1b36')
    # Solid catalyst slab at bottom
    slab = plt.Rectangle((0.2, 0.2), 3.6, 1.2, facecolor='#90a4ae', edgecolor='#37474f', lw=1.5)
    ax.add_patch(slab)
    ax.text(2.0, 0.6, 'Solid Catalyst\nActive Surface', ha='center', va='center', fontsize=6.5, fontweight='bold', color='#263238')

# Panel 1: Molecules approaching and adsorbing
ax1.plot([1.2, 1.2], [3.2, 1.8], '->', color='#1565c0', lw=1.5)
ax1.scatter([1.0, 1.4], [3.2, 3.2], s=50, color='#1565c0', zorder=5) # A2
ax1.plot([2.8, 2.8], [3.0, 1.8], '->', color='#a81717', lw=1.5)
ax1.scatter([2.6, 3.0], [3.0, 3.0], s=50, color='#a81717', zorder=5) # B2

# Panel 2: Adsorbed and bonds stretching
for x, c in [(1.0, '#1565c0'), (1.6, '#1565c0'), (2.4, '#a81717'), (3.0, '#a81717')]:
    ax2.plot([x, x], [1.4, 1.9], ':', color='#212121', lw=1.2)
    ax2.scatter(x, 1.9, s=50, color=c, zorder=5)

# Panel 3: New bonds forming between A and B
ax3.scatter(1.3, 1.9, s=50, color='#1565c0', zorder=5)
ax3.scatter(1.7, 1.9, s=50, color='#a81717', zorder=5)
ax3.plot([1.3, 1.7], [1.9, 1.9], color='#212121', lw=2.0)

ax3.scatter(2.3, 1.9, s=50, color='#1565c0', zorder=5)
ax3.scatter(2.7, 1.9, s=50, color='#a81717', zorder=5)
ax3.plot([2.3, 2.7], [1.9, 1.9], color='#212121', lw=2.0)

# Panel 4: Desorption of AB products
ax4.plot([1.5, 1.5], [2.0, 3.2], '->', color='#2e7d32', lw=1.5)
ax4.scatter(1.3, 3.2, s=50, color='#1565c0', zorder=5)
ax4.scatter(1.7, 3.2, s=50, color='#a81717', zorder=5)
ax4.plot([1.3, 1.7], [3.2, 3.2], color='#2e7d32', lw=2.0)

ax4.plot([2.5, 2.5], [2.0, 3.2], '->', color='#2e7d32', lw=1.5)
ax4.scatter(2.3, 3.2, s=50, color='#1565c0', zorder=5)
ax4.scatter(2.7, 3.2, s=50, color='#a81717', zorder=5)
ax4.plot([2.3, 2.7], [3.2, 3.2], color='#2e7d32', lw=2.0)

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'heterogeneous_catalysis_steps.png'), dpi=200)
plt.close(fig)

print("Generated Topic 8 figures successfully!")
