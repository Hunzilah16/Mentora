"""
Generate high-resolution figures for Topic 9: Chemical Periodicity.
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

elements = ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar']
x_vals = np.arange(len(elements))

# -------------------------------------------------------------
# Figure 1: 4-Panel Physical Property Trends Across Period 3
# -------------------------------------------------------------
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(7.2, 4.4), dpi=200)

# Panel 1: Atomic Radius (pm)
r_atomic = [186, 160, 143, 118, 110, 102, 99, 95]
ax1.plot(x_vals, r_atomic, 'o-', color='#1565c0', lw=1.8, markersize=5)
ax1.set_title('Atomic Radius / pm', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax1.set_xticks(x_vals)
ax1.set_xticklabels(elements, fontsize=7.5)
ax1.set_ylim(80, 200)
ax1.grid(True, linestyle=':', alpha=0.6)

# Panel 2: First Ionisation Energy (kJ/mol)
ie1 = [496, 738, 578, 789, 1012, 1000, 1251, 1521]
ax2.plot(x_vals, ie1, 's-', color='#a81717', lw=1.8, markersize=5)
ax2.set_title(r'First Ionisation Energy / $\mathrm{kJ\ mol^{-1}}$', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax2.set_xticks(x_vals)
ax2.set_xticklabels(elements, fontsize=7.5)
ax2.set_ylim(400, 1650)
ax2.grid(True, linestyle=':', alpha=0.6)
# Dips
ax2.annotate(r'3p subshell' '\n' r'shielding', xy=(2, 578), xytext=(1.8, 380),
             arrowprops=dict(arrowstyle='->', color='#a81717', lw=1), fontsize=6.5, color='#a81717')
ax2.annotate(r'3p electron' '\n' r'pair repulsion', xy=(5, 1000), xytext=(4.2, 1200),
             arrowprops=dict(arrowstyle='->', color='#a81717', lw=1), fontsize=6.5, color='#a81717')

# Panel 3: Melting Point (K)
mp = [371, 923, 933, 1687, 317, 392, 172, 84]
ax3.plot(x_vals, mp, '^-', color='#2e7d32', lw=1.8, markersize=5)
ax3.set_title('Melting Point / K', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax3.set_xticks(x_vals)
ax3.set_xticklabels(elements, fontsize=7.5)
ax3.set_ylim(0, 1800)
ax3.grid(True, linestyle=':', alpha=0.6)
ax3.text(3, 1700, 'Si: Giant Covalent', ha='center', fontsize=6.5, fontweight='bold', color='#2e7d32')
ax3.text(5, 450, r'$\mathrm{S_8} > \mathrm{P_4}$', ha='center', fontsize=6.5, fontweight='bold', color='#e65100')

# Panel 4: Electrical Conductivity (relative)
cond = [21, 36, 61, 0.001, 0, 0, 0, 0]
ax4.bar(x_vals, cond, color='#e65100', width=0.5, edgecolor='#bf360c')
ax4.set_title('Electrical Conductivity (relative)', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax4.set_xticks(x_vals)
ax4.set_xticklabels(elements, fontsize=7.5)
ax4.set_ylim(0, 70)
ax4.grid(True, linestyle=':', alpha=0.6)
ax4.text(2, 63, r'Al: $3\ \mathrm{e^-}$ per atom', ha='center', fontsize=6.5, fontweight='bold', color='#e65100')

plt.suptitle('Periodicity of Physical Properties Across Period 3 Elements', fontsize=10, fontweight='bold', color='#0b1b36')
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'period3_physical_trends.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 2: Ionic Radii Across Period 3 (Cations vs Anions)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=200)

ions_cat = ['Na⁺', 'Mg²⁺', 'Al³⁺']
r_cat = [102, 72, 54] # pm
x_cat = [0, 1, 2]

ions_an = ['P³⁻', 'S²⁻', 'Cl⁻']
r_an = [212, 184, 181] # pm
x_an = [4, 5, 6]

ax.plot(x_cat, r_cat, 'o-', color='#1565c0', lw=2.2, markersize=8, label=r'Cations ($\mathrm{Na^+, Mg^{2+}, Al^{3+}}$: $[\mathrm{Ne}]$ core)')
ax.plot(x_an, r_an, 's-', color='#c62828', lw=2.2, markersize=8, label=r'Anions ($\mathrm{P^{3-}, S^{2-}, Cl^-}$: $[\mathrm{Ar}]$ core)')

# Labels on points
for x, y, ion in zip(x_cat, r_cat, ions_cat):
    ax.text(x, y - 18, f'{ion}\n({y} pm)', ha='center', fontsize=7.5, fontweight='bold', color='#1565c0')
for x, y, ion in zip(x_an, r_an, ions_an):
    ax.text(x, y + 8, f'{ion}\n({y} pm)', ha='center', fontsize=7.5, fontweight='bold', color='#c62828')

# Discontinuity arrow
ax.annotate('Sharp increase:\nAnions have 3 shells\nplus electron repulsion', xy=(4, 212), xytext=(2.5, 140),
            arrowprops=dict(arrowstyle='->', color='#212121', lw=1.5),
            fontsize=7.5, fontweight='bold', color='#212121')

ax.set_title('Comparison of Ionic Radii Across Period 3', fontsize=10, fontweight='bold', color='#0b1b36', pad=10)
ax.set_ylabel('Ionic Radius / pm', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_xlim(-0.5, 7.5)
ax.set_ylim(20, 250)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6])
ax.set_xticklabels(['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl'], fontsize=8.5, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6, color='#99aab5')
ax.legend(frameon=True, facecolor='#f8f9fa', fontsize=7.5, loc='upper left')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'period3_ionic_radii.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 3: Period 3 Oxides: Acid-Base Continuum
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.8, 2.8), dpi=200)
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(0, 5)
ax.axis('off')

# Gradient background bar
ox_labels = [r'$\mathrm{Na_2O}$', r'$\mathrm{MgO}$', r'$\mathrm{Al_2O_3}$', r'$\mathrm{SiO_2}$', r'$\mathrm{P_4O_{10}}$', r'$\mathrm{SO_2}$', r'$\mathrm{SO_3}$']
types = ['Basic\n(Giant Ionic)', 'Basic\n(Giant Ionic)', 'Amphoteric\n(Giant Ionic)', 'Acidic\n(Giant Covalent)', 'Acidic\n(Molecular)', 'Acidic\n(Molecular)', 'Acidic\n(Molecular)']
colors = ['#1565c0', '#1e88e5', '#7b1fa2', '#d32f2f', '#c62828', '#b71c1c', '#880e4f']
ph_vals = ['pH 14', 'pH 9', 'Insoluble', 'Insoluble', 'pH 1-2', 'pH 2-3', 'pH 1']

for i in range(7):
    box = plt.Rectangle((i - 0.4, 1.2), 0.8, 2.6, facecolor=colors[i], alpha=0.15, edgecolor=colors[i], lw=1.5)
    ax.add_patch(box)
    ax.text(i, 3.2, ox_labels[i], ha='center', fontsize=9.5, fontweight='bold', color=colors[i])
    ax.text(i, 2.2, types[i], ha='center', fontsize=6.5, fontweight='semibold', color='#212121')
    ax.text(i, 1.4, ph_vals[i], ha='center', fontsize=7.5, fontweight='bold', color=colors[i])

# Arrow across bottom
ax.annotate('', xy=(6.2, 0.6), xytext=(-0.2, 0.6), arrowprops=dict(arrowstyle='->', lw=2.0, color='#0b1b36'))
ax.text(3.0, 0.2, 'Increasingly Acidic Nature Across Period 3 (Basic -> Amphoteric -> Acidic)',
        ha='center', fontsize=8, fontweight='bold', color='#0b1b36')

ax.set_title('Periodicity of Acid-Base Character of Period 3 Oxides', fontsize=10, fontweight='bold', color='#0b1b36')
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'period3_oxides_acid_base.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 4: Period 3 Chlorides Hydrolysis Summary
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.8, 2.8), dpi=200)
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(0, 5)
ax.axis('off')

ch_labels = [r'$\mathrm{NaCl}$', r'$\mathrm{MgCl_2}$', r'$\mathrm{Al_2Cl_6}$', r'$\mathrm{SiCl_4}$', r'$\mathrm{PCl_3}$', r'$\mathrm{PCl_5}$']
ch_types = ['Giant Ionic', 'Giant Ionic', 'Covalent Dimer', 'Simple Covalent', 'Simple Covalent', 'Simple Covalent']
ch_action = ['Dissolves\n(No hydrolysis)', 'Slight\nhydrolysis', 'Vigorous\nhydrolysis', 'Violent\nhydrolysis', 'Violent\nhydrolysis', 'Violent\nhydrolysis']
ch_ph = ['pH 7', 'pH 6.5', 'pH 3 (HCl fumes)', 'pH 1-2 (white SiO2)', 'pH 1-2 (HCl fumes)', 'pH 1-2 (HCl fumes)']
ch_colors = ['#2e7d32', '#388e3c', '#e65100', '#c62828', '#b71c1c', '#880e4f']

for i in range(6):
    box = plt.Rectangle((i - 0.4, 1.0), 0.8, 3.0, facecolor=ch_colors[i], alpha=0.15, edgecolor=ch_colors[i], lw=1.5)
    ax.add_patch(box)
    ax.text(i, 3.4, ch_labels[i], ha='center', fontsize=9.5, fontweight='bold', color=ch_colors[i])
    ax.text(i, 2.7, ch_types[i], ha='center', fontsize=6.5, color='#424242')
    ax.text(i, 1.9, ch_action[i], ha='center', fontsize=6.5, fontweight='semibold', color='#212121')
    ax.text(i, 1.2, ch_ph[i], ha='center', fontsize=6.5, fontweight='bold', color=ch_colors[i])

ax.annotate('', xy=(5.2, 0.4), xytext=(-0.2, 0.4), arrowprops=dict(arrowstyle='->', lw=2.0, color='#0b1b36'))
ax.text(2.5, 0.1, 'Increasing Hydrolysis & Acidity with Water (Neutral -> Weakly Acidic -> Highly Acidic)',
        ha='center', fontsize=7.5, fontweight='bold', color='#0b1b36')

ax.set_title('Reactions of Period 3 Chlorides with Water: Structure & Hydrolysis', fontsize=10, fontweight='bold', color='#0b1b36')
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'period3_chlorides_hydrolysis.png'), dpi=200)
plt.close(fig)

print("Generated Topic 9 figures successfully!")
