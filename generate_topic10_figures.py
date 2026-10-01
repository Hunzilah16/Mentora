"""
Generate high-DPI figures for Topic 10: Group 2.
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial'],
    'axes.edgecolor': '#0b1b36',
    'axes.linewidth': 1.2,
    'grid.color': '#e2e8f0',
    'grid.linestyle': '--',
    'grid.alpha': 0.7,
})

def make_thermal_decomposition():
    fig, ax = plt.subplots(figsize=(7, 4.2), dpi=300)
    elements = ['Mg', 'Ca', 'Sr', 'Ba']
    # Decomposition temperatures of carbonates in °C
    temp_carb = [540, 900, 1290, 1360]
    # Decomposition temperatures of nitrates in °C
    temp_nitr = [350, 500, 570, 600]
    
    x = np.arange(len(elements))
    width = 0.35
    
    rects1 = ax.bar(x - width/2, temp_carb, width, label='Carbonates ($MCO_3$)', color='#a81717', edgecolor='#0b1b36', linewidth=1.2)
    rects2 = ax.bar(x + width/2, temp_nitr, width, label='Nitrates ($M(NO_3)_2$)', color='#0b1b36', edgecolor='#0b1b36', linewidth=1.2)
    
    for r in rects1:
        h = r.get_height()
        ax.annotate(f'{h} °C', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#a81717')
    for r in rects2:
        h = r.get_height()
        ax.annotate(f'{h} °C', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#0b1b36')
        
    ax.set_title("Thermal Stability of Group 2 Carbonates and Nitrates", fontsize=11, fontweight='bold', color='#0b1b36', pad=12)
    ax.set_xlabel("Group 2 Cation ($M^{2+}$)", fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax.set_ylabel("Decomposition Temperature / °C", fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax.set_xticks(x)
    ax.set_xticklabels([r'$\mathbf{Mg^{2+}}$', r'$\mathbf{Ca^{2+}}$', r'$\mathbf{Sr^{2+}}$', r'$\mathbf{Ba^{2+}}$'], fontsize=10)
    ax.set_ylim(0, 1600)
    ax.grid(True, axis='y')
    ax.legend(frameon=True, facecolor='white', edgecolor='#0b1b36', fontsize=9)
    
    # Text annotation explaining trend
    ax.text(0.05, 0.82, "Down Group 2:\n• Cation radius increases ($Mg^{2+} \\rightarrow Ba^{2+}$)\n• Charge density decreases\n• Less polarising power on $CO_3^{2-}$ / $NO_3^-$\n• Higher temperature needed to decompose",
            transform=ax.transAxes, fontsize=8, verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    plt.tight_layout()
    plt.savefig("figures/group2_thermal_decomposition.png")
    plt.close()
    print("Generated figures/group2_thermal_decomposition.png")

def make_solubility_trends():
    fig, ax1 = plt.subplots(figsize=(7, 4.2), dpi=300)
    
    elements = ['Mg', 'Ca', 'Sr', 'Ba']
    # Solubility of hydroxides (mol / 100g H2O at 20°C, arbitrary/log scaled for clear trend)
    # Mg(OH)2: 1.5e-4, Ca(OH)2: 2.3e-2, Sr(OH)2: 6.6e-2, Ba(OH)2: 2.3e-1
    sol_hydroxide = [0.00015, 0.023, 0.066, 0.23]
    # Solubility of sulfates (g / 100g H2O at 20°C)
    # MgSO4: 35.7, CaSO4: 0.21, SrSO4: 0.013, BaSO4: 0.00025
    sol_sulfate = [35.7, 0.21, 0.013, 0.00025]
    
    x = np.arange(len(elements))
    
    color_oh = '#0b1b36'
    color_so4 = '#a81717'
    
    line1 = ax1.plot(x, sol_hydroxide, marker='o', linewidth=2.2, markersize=8, color=color_oh, label='Hydroxides, $M(OH)_2$ (increases down group)')
    ax1.set_ylabel('Solubility of Hydroxides / $\\mathrm{mol\\cdot dm^{-3}}$', color=color_oh, fontsize=9.5, fontweight='bold')
    ax1.set_yscale('log')
    ax1.tick_params(axis='y', labelcolor=color_oh)
    ax1.set_xlabel('Group 2 Element', fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax1.set_xticks(x)
    ax1.set_xticklabels(elements, fontsize=10, fontweight='bold')
    
    ax2 = ax1.twinx()
    line2 = ax2.plot(x, sol_sulfate, marker='s', linewidth=2.2, markersize=8, color=color_so4, linestyle='--', label='Sulfates, $MSO_4$ (decreases down group)')
    ax2.set_ylabel('Solubility of Sulfates / $\\mathrm{g / 100g\\ H_2O}$', color=color_so4, fontsize=9.5, fontweight='bold')
    ax2.set_yscale('log')
    ax2.tick_params(axis='y', labelcolor=color_so4)
    
    # Combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='center left', frameon=True, facecolor='white', edgecolor='#0b1b36', fontsize=8.5)
    
    plt.title("Opposing Trends in Solubility of Group 2 Hydroxides vs Sulfates", fontsize=11, fontweight='bold', color='#0b1b36', pad=12)
    plt.tight_layout()
    plt.savefig("figures/group2_solubility_trends.png")
    plt.close()
    print("Generated figures/group2_solubility_trends.png")

def make_reactivity_water():
    fig, ax = plt.subplots(figsize=(7, 4.2), dpi=300)
    
    # Visual comparison diagram for reactions with water
    elements = ['Mg', 'Ca', 'Sr', 'Ba']
    rates = [1, 5, 8, 10] # relative vigour of reaction with cold water
    colors = ['#94a3b8', '#38bdf8', '#0284c7', '#0b1b36']
    
    bars = ax.barh(elements, rates, color=colors, edgecolor='#0b1b36', height=0.55, linewidth=1.2)
    
    ax.set_xlabel("Relative Vigour of Reaction with Cold Water", fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax.set_title("Trend in Reactivity of Group 2 Elements with Cold Water", fontsize=11, fontweight='bold', color='#0b1b36', pad=12)
    
    observations = [
        "Very slow; few bubbles; reacts rapidly with steam to form white MgO + H₂",
        "Steady effervescence; cloudy suspension of Ca(OH)₂ formed; pH ≈ 11",
        "Vigorous fizzing; dissolves to give clear solution of Sr(OH)₂; pH ≈ 13",
        "Very vigorous / rapid effervescence; highly soluble Ba(OH)₂ forms clear solution; pH ≈ 14"
    ]
    
    for i, (bar, obs) in enumerate(zip(bars, observations)):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                obs, ha='left', va='center', fontsize=7.8, color='#0b1b36')
        
    ax.set_xlim(0, 16)
    ax.set_xticks(range(0, 11, 2))
    ax.grid(True, axis='x')
    
    # Annotate explanation
    ax.text(0.05, 0.12, "Reactivity increases down group as first two ionisation energies decrease\n(atomic radius increases, electron shielding increases, easier to lose 2 valence electrons).",
            transform=ax.transAxes, fontsize=8, style='italic', color='#475569',
            bbox=dict(boxstyle='square,pad=0.4', facecolor='#f1f5f9', edgecolor='#cbd5e1'))
    
    plt.tight_layout()
    plt.savefig("figures/group2_reactivity_water.png")
    plt.close()
    print("Generated figures/group2_reactivity_water.png")

def make_enthalpy_solubility():
    fig, ax = plt.subplots(figsize=(7, 4.2), dpi=300)
    
    elements = ['Mg', 'Ca', 'Sr', 'Ba']
    # Hydration enthalpy (magnitude kJ/mol)
    hyd_M2 = [1920, 1577, 1443, 1305]
    # Lattice enthalpy of hydroxide (magnitude kJ/mol)
    lat_OH = [2995, 2630, 2465, 2250]
    # Lattice enthalpy of sulfate (magnitude kJ/mol)
    lat_SO4 = [2850, 2600, 2450, 2350]
    
    x = np.arange(len(elements))
    
    ax.plot(x, hyd_M2, marker='o', color='#a81717', linewidth=2, label='Hydration Enthalpy of $M^{2+}$ (magnitude decreases)')
    ax.plot(x, [h - 1000 for h in lat_SO4], marker='^', color='#0b1b36', linewidth=2, linestyle='--', label='Lattice Enthalpy change offset')
    
    ax.set_xticks(x)
    ax.set_xticklabels([r'$\mathbf{Mg^{2+}}$', r'$\mathbf{Ca^{2+}}$', r'$\mathbf{Sr^{2+}}$', r'$\mathbf{Ba^{2+}}$'], fontsize=10)
    ax.set_ylabel("Magnitude of Enthalpy / $\\mathrm{kJ\\cdot mol^{-1}}$", fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax.set_xlabel("Group 2 Cation", fontsize=9.5, fontweight='bold', color='#0b1b36')
    ax.set_title("Enthalpy Factors Explaining Group 2 Sulfate Solubility", fontsize=11, fontweight='bold', color='#0b1b36', pad=12)
    
    ax.text(0.05, 0.25, "Why $MSO_4$ solubility decreases down Group 2:\n• Sulfate ion ($SO_4^{2-}$) is large; lattice enthalpy decreases very little\n• Cation hydration enthalpy decreases sharply ($Mg^{2+} \\rightarrow Ba^{2+}$)\n• Thus $\\Delta H_{\\mathrm{sol}} = \\Delta H_{\\mathrm{hyd}} - \\Delta H_{\\mathrm{latt}}$ becomes more endothermic (less favorable)",
            transform=ax.transAxes, fontsize=8.2, verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fffbeb', edgecolor='#f59e0b'))
    
    ax.grid(True)
    ax.legend(loc='upper right', fontsize=8.5, frameon=True, facecolor='white', edgecolor='#0b1b36')
    
    plt.tight_layout()
    plt.savefig("figures/group2_enthalpy_solubility.png")
    plt.close()
    print("Generated figures/group2_enthalpy_solubility.png")

if __name__ == "__main__":
    make_thermal_decomposition()
    make_solubility_trends()
    make_reactivity_water()
    make_enthalpy_solubility()
