"""
Generate high-resolution figures for Topic 5: Chemical Energetics.
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
# Figure 1: Enthalpy Profiles (Exothermic & Endothermic + Catalysed)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.2), dpi=200)

# Exothermic
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Exothermic Reaction', fontsize=9.5, fontweight='bold', color='#0b1b36')

# Enthalpy profile uncatalysed
x_uncat = np.linspace(2.5, 7.5, 100)
y_uncat = 5.0 + 3.8 * np.sin(np.pi * (x_uncat - 2.5) / 5.0)
ax1.plot([0.5, 2.5], [5.0, 5.0], color='#0b1b36', lw=2.5) # Reactants
ax1.plot(x_uncat, y_uncat, color='#a81717', lw=2.0, label='Uncatalysed')
# Catalysed
y_cat = 5.0 + 2.2 * np.sin(np.pi * (x_uncat - 2.5) / 5.0)
ax1.plot(x_uncat, y_cat, color='#2e7d32', lw=2.0, linestyle='--', label='Catalysed')
ax1.plot([7.5, 9.5], [2.0, 2.0], color='#0b1b36', lw=2.5) # Products

ax1.text(1.5, 5.3, 'Reactants', ha='center', fontsize=8, fontweight='bold', color='#0b1b36')
ax1.text(8.5, 2.3, 'Products', ha='center', fontsize=8, fontweight='bold', color='#0b1b36')

# Arrows for Ea and Delta H
ax1.annotate('', xy=(5.0, 8.8), xytext=(5.0, 5.0), arrowprops=dict(arrowstyle='<->', color='#a81717', lw=1.2))
ax1.text(5.3, 6.8, r'$E_\mathrm{a}$', fontsize=8.5, fontweight='bold', color='#a81717')

ax1.annotate('', xy=(5.0, 7.2), xytext=(5.0, 5.0), arrowprops=dict(arrowstyle='<->', color='#2e7d32', lw=1.2))
ax1.text(4.4, 6.0, r"$E'_\mathrm{a}$", fontsize=8.5, fontweight='bold', color='#2e7d32')

ax1.annotate('', xy=(8.5, 2.0), xytext=(8.5, 5.0), arrowprops=dict(arrowstyle='<->', color='#0b1b36', lw=1.2))
ax1.text(8.8, 3.5, r'$\Delta H < 0$' '\n(released)', fontsize=8, fontweight='bold', color='#0b1b36')
ax1.legend(frameon=True, facecolor='#f8f9fa', fontsize=7.5, loc='upper left')

# Endothermic
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Endothermic Reaction', fontsize=9.5, fontweight='bold', color='#0b1b36')

# Enthalpy profile uncatalysed
y_endo = 2.0 + 6.5 * np.sin(np.pi * (x_uncat - 2.5) / 5.0)
ax2.plot([0.5, 2.5], [2.0, 2.0], color='#0b1b36', lw=2.5) # Reactants
ax2.plot(x_uncat, y_endo, color='#a81717', lw=2.0)
ax2.plot([7.5, 9.5], [5.5, 5.5], color='#0b1b36', lw=2.5) # Products

ax2.text(1.5, 2.3, 'Reactants', ha='center', fontsize=8, fontweight='bold', color='#0b1b36')
ax2.text(8.5, 5.8, 'Products', ha='center', fontsize=8, fontweight='bold', color='#0b1b36')

# Arrows for Ea and Delta H
ax2.annotate('', xy=(5.0, 8.5), xytext=(5.0, 2.0), arrowprops=dict(arrowstyle='<->', color='#a81717', lw=1.2))
ax2.text(5.3, 5.0, r'$E_\mathrm{a}$', fontsize=8.5, fontweight='bold', color='#a81717')

ax2.annotate('', xy=(8.5, 5.5), xytext=(8.5, 2.0), arrowprops=dict(arrowstyle='<->', color='#0b1b36', lw=1.2))
ax2.text(8.8, 3.7, r'$\Delta H > 0$' '\n(absorbed)', fontsize=8, fontweight='bold', color='#0b1b36')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'reaction_profile_exo_endo.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 2: Hess's Law Thermochemical Cycles
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.0), dpi=200)

# Cycle 1: Formation
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 8)
ax1.axis('off')
ax1.set_title(r"Hess's Law: Enthalpy of Formation ($\Delta H_\mathrm{f}^\circ$)", fontsize=8.5, fontweight='bold', color='#0b1b36')

# Reactants -> Products (top horizontal)
ax1.text(2.0, 6.5, 'REACTANTS', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0b1b36',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#e3f2fd', edgecolor='#0b1b36'))
ax1.text(8.0, 6.5, 'PRODUCTS', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0b1b36',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#e3f2fd', edgecolor='#0b1b36'))
ax1.annotate('', xy=(6.5, 6.5), xytext=(3.5, 6.5), arrowprops=dict(arrowstyle='->', lw=2.0, color='#0b1b36'))
ax1.text(5.0, 7.1, r'$\Delta H_\mathrm{r}^\circ$', ha='center', fontsize=9, fontweight='bold', color='#0b1b36')

# Elements (bottom)
ax1.text(5.0, 1.8, 'ELEMENTS\n(standard states)', ha='center', va='center', fontsize=8, fontweight='bold', color='#a81717',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffebee', edgecolor='#a81717'))

# Arrows from elements to reactants and products
ax1.annotate('', xy=(2.0, 5.8), xytext=(4.0, 2.5), arrowprops=dict(arrowstyle='->', lw=1.8, color='#a81717'))
ax1.text(2.0, 3.8, r'$\sum \Delta H_\mathrm{f}^\circ(\mathrm{react})$', ha='center', fontsize=7.5, color='#a81717')

ax1.annotate('', xy=(8.0, 5.8), xytext=(6.0, 2.5), arrowprops=dict(arrowstyle='->', lw=1.8, color='#a81717'))
ax1.text(8.0, 3.8, r'$\sum \Delta H_\mathrm{f}^\circ(\mathrm{prod})$', ha='center', fontsize=7.5, color='#a81717')

ax1.text(5.0, 0.4, r'$\Delta H_\mathrm{r}^\circ = \sum \Delta H_\mathrm{f}^\circ(\mathrm{prod}) - \sum \Delta H_\mathrm{f}^\circ(\mathrm{react})$',
         ha='center', fontsize=7.5, fontweight='bold', color='#0b1b36')

# Cycle 2: Combustion
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 8)
ax2.axis('off')
ax2.set_title(r"Hess's Law: Enthalpy of Combustion ($\Delta H_\mathrm{c}^\circ$)", fontsize=8.5, fontweight='bold', color='#0b1b36')

# Reactants -> Products (top horizontal)
ax2.text(2.0, 6.5, 'REACTANTS', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0b1b36',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#e8f5e9', edgecolor='#2e7d32'))
ax2.text(8.0, 6.5, 'PRODUCTS', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0b1b36',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#e8f5e9', edgecolor='#2e7d32'))
ax2.annotate('', xy=(6.5, 6.5), xytext=(3.5, 6.5), arrowprops=dict(arrowstyle='->', lw=2.0, color='#0b1b36'))
ax2.text(5.0, 7.1, r'$\Delta H_\mathrm{r}^\circ$', ha='center', fontsize=9, fontweight='bold', color='#0b1b36')

# Combustion products (bottom)
ax2.text(5.0, 1.8, 'COMBUSTION\nPRODUCTS\n(CO2 + H2O)', ha='center', va='center', fontsize=8, fontweight='bold', color='#e65100',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff3e0', edgecolor='#e65100'))

# Arrows DOWN from reactants and products to combustion products
ax2.annotate('', xy=(4.0, 2.7), xytext=(2.0, 5.8), arrowprops=dict(arrowstyle='->', lw=1.8, color='#e65100'))
ax2.text(2.0, 4.0, r'$\sum \Delta H_\mathrm{c}^\circ(\mathrm{react})$', ha='center', fontsize=7.5, color='#e65100')

ax2.annotate('', xy=(6.0, 2.7), xytext=(8.0, 5.8), arrowprops=dict(arrowstyle='->', lw=1.8, color='#e65100'))
ax2.text(8.0, 4.0, r'$\sum \Delta H_\mathrm{c}^\circ(\mathrm{prod})$', ha='center', fontsize=7.5, color='#e65100')

ax2.text(5.0, 0.4, r'$\Delta H_\mathrm{r}^\circ = \sum \Delta H_\mathrm{c}^\circ(\mathrm{react}) - \sum \Delta H_\mathrm{c}^\circ(\mathrm{prod})$',
         ha='center', fontsize=7.5, fontweight='bold', color='#0b1b36')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'hess_law_cycles.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 3: Calorimetry Cooling Curve & Delta T Extrapolation
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=200)

t = np.array([0, 1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9, 10])
# Constant initial T = 20.0 °C for t = 0, 1, 2
# Reactant added at t = 3.0 min
# Actual T measured from t = 3.5 min onwards: 34.5, 33.8, 32.6, 31.5, 30.4, 29.3, 28.2
temp_actual = np.array([20.0, 20.0, 20.0, np.nan, 34.2, 33.6, 32.5, 31.4, 30.3, 29.2, 28.1, 27.0])

ax.plot(t[:3], temp_actual[:3], 'o-', color='#0b1b36', label='Initial temperature', lw=1.5, markersize=5)
ax.plot(t[4:], temp_actual[4:], 's-', color='#a81717', label='Measured cooling data', lw=1.5, markersize=5)

# Extrapolation line back to t = 3 min
t_extrap = np.linspace(3.0, 10.0, 50)
temp_extrap = 38.0 - 1.1 * t_extrap
ax.plot(t_extrap, temp_extrap, '--', color='#1e88e5', lw=2.0, label='Extrapolated cooling curve')

# Extrapolated T at t = 3.0
t_max_extrap = 38.0 - 1.1 * 3.0 # = 34.7 °C
ax.plot(3.0, t_max_extrap, '*', color='#ff9800', markersize=12, label=r'Corrected $T_\mathrm{max}$ (34.7 °C)')

# Initial T extrapolation to t = 3.0
ax.plot([2.0, 3.0], [20.0, 20.0], ':', color='#0b1b36', lw=1.5)

# Vertical line at mixing time t = 3.0 min
ax.axvline(3.0, color='#666666', linestyle=':', lw=1.2)
ax.text(3.1, 21.0, 'Reactant added\nat t = 3 min', fontsize=7.5, color='#333333', fontweight='semibold')

# Delta T arrow
ax.annotate('', xy=(3.0, t_max_extrap), xytext=(3.0, 20.0),
            arrowprops=dict(arrowstyle='<->', color='#a81717', lw=1.8))
ax.text(3.2, 27.0, r'$\Delta T_\mathrm{corrected} = 14.7\ ^\circ\mathrm{C}$', fontsize=8.5, fontweight='bold', color='#a81717')

ax.set_title(r'Calorimetry Cooling Curve: Determining Corrected $\Delta T$', fontsize=10, fontweight='bold', color='#0b1b36', pad=10)
ax.set_xlabel('Time / minutes', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_ylabel(r'Temperature / $^\circ\mathrm{C}$', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(18.0, 37.0)
ax.grid(True, linestyle=':', alpha=0.6, color='#99aab5')
ax.legend(frameon=True, facecolor='#f8f9fa', fontsize=7.5, loc='upper right')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'calorimetry_cooling_curve.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 4: Spirit Burner Combustion Calorimeter
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.0, 3.2), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Copper calorimeter (can)
can = plt.Rectangle((3.5, 3.2), 3.0, 3.0, facecolor='#d7ccc8', edgecolor='#5d4037', lw=1.8)
ax.add_patch(can)
# Water inside
water = plt.Rectangle((3.6, 3.3), 2.8, 2.5, facecolor='#bbdefb', edgecolor='none')
ax.add_patch(water)
ax.text(5.0, 4.5, 'Known volume\nof water (m)', ha='center', fontsize=8, fontweight='bold', color='#0d47a1')

# Thermometer
ax.plot([5.8, 5.8], [3.8, 6.8], color='#c62828', lw=2.5)
ax.text(6.0, 6.5, 'Thermometer\n(measures Delta T)', fontsize=7.5, color='#c62828')

# Draught shield
ax.plot([2.5, 2.5], [1.5, 6.2], color='#78909c', lw=2.0, linestyle='--')
ax.plot([7.5, 7.5], [1.5, 6.2], color='#78909c', lw=2.0, linestyle='--')
ax.text(2.3, 4.0, 'Draught\nshield', ha='right', fontsize=7.5, color='#455a64')

# Spirit burner
burner = plt.Rectangle((4.2, 0.8), 1.6, 1.4, facecolor='#cfd8dc', edgecolor='#37474f', lw=1.5)
ax.add_patch(burner)
# Wick
ax.plot([5.0, 5.0], [2.2, 2.5], color='#424242', lw=2.5)
# Flame
flame = plt.Polygon([[5.0, 3.1], [4.6, 2.5], [5.4, 2.5]], facecolor='#ff7043', edgecolor='#d84315', lw=1)
ax.add_patch(flame)
ax.text(5.0, 1.4, 'Spirit burner\n(liquid fuel)', ha='center', fontsize=7.5, fontweight='bold', color='#263238')

# Copper can label
ax.text(3.3, 5.5, 'Copper can\ncalorimeter', ha='right', fontsize=7.5, color='#5d4037', fontweight='semibold')

ax.set_title('Experimental Setup: Determining Enthalpy of Combustion', fontsize=10, fontweight='bold', color='#0b1b36')
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'flame_calorimeter_setup.png'), dpi=200)
plt.close(fig)

print("Generated Topic 5 figures successfully!")
