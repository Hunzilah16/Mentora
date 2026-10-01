"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for Topic 23: Chemical Energetics
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
# Figure 1: Born-Haber Cycle for ZnS (Q1)
# -----------------------------------------------------------------------------
def create_born_haber_zns():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(-500, 4000)
    ax.axis('off')

    # Energy Levels
    # Level 0: Elements in standard states
    ax.plot([0.5, 3.0], [0, 0], color='#0b1b36', lw=2.0)
    ax.text(1.75, 50, r'$\mathrm{Zn(s)} + \mathrm{S(s)}$', ha='center', fontsize=7.5, fontweight='bold', color='#0b1b36')

    # Level -1: Solid Compound ZnS(s)
    ax.plot([0.5, 3.0], [-206, -206], color='#a81717', lw=2.0)
    ax.text(1.75, -280, r'$\mathrm{ZnS(s)}$', ha='center', fontsize=7.5, fontweight='bold', color='#a81717')

    # Level 1: Atomisation of Zn
    ax.plot([3.4, 5.4], [131, 131], color='#0b1b36', lw=1.8)
    ax.text(4.4, 180, r'$\mathrm{Zn(g)} + \mathrm{S(s)}$', ha='center', fontsize=7.0, color='#0b1b36')

    # Level 2: Atomisation of S
    ax.plot([3.4, 5.4], [410, 410], color='#0b1b36', lw=1.8)
    ax.text(4.4, 460, r'$\mathrm{Zn(g)} + \mathrm{S(g)}$', ha='center', fontsize=7.0, color='#0b1b36')

    # Level 3: Ionisation of Zn (1st + 2nd IE)
    ax.plot([5.8, 8.2], [3050, 3050], color='#0b1b36', lw=1.8)
    ax.text(7.0, 3110, r'$\mathrm{Zn^{2+}(g)} + \mathrm{S(g)} + 2\mathrm{e^-}$', ha='center', fontsize=7.0, color='#0b1b36')

    # Level 4: Electron Affinity of S (1st + 2nd EA)
    ax.plot([6.8, 9.5], [3382, 3382], color='#0b1b36', lw=2.0)
    ax.text(8.15, 3440, r'$\mathrm{Zn^{2+}(g)} + \mathrm{S^{2-}(g)}$', ha='center', fontsize=7.5, fontweight='bold', color='#0b1b36')

    # Arrows
    # Formation: Elements -> ZnS(s)
    ax.annotate('', xy=(1.0, -206), xytext=(1.0, 0), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.3))
    ax.text(0.3, -110, r'$\Delta H^\circ_\mathrm{f} = -206$', fontsize=6.8, color='#a81717', fontweight='bold', va='center')

    # Atomisation of Zn
    ax.annotate('', xy=(3.4, 131), xytext=(3.0, 0), arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.1))
    ax.text(3.1, 55, r'$+131$', fontsize=6.5, color='#2e7d32')

    # Atomisation of S
    ax.annotate('', xy=(4.4, 410), xytext=(4.4, 131), arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.1))
    ax.text(4.5, 260, r'$+279$', fontsize=6.5, color='#2e7d32')

    # IE of Zn
    ax.annotate('', xy=(6.2, 3050), xytext=(5.4, 410), arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.1))
    ax.text(5.3, 1750, r'$\mathrm{IE}_1 + \mathrm{IE}_2 = +2640$', fontsize=6.5, color='#1565c0', rotation=70)

    # EA of S
    ax.annotate('', xy=(8.1, 3382), xytext=(8.1, 3050), arrowprops=dict(arrowstyle='->', color='#e65100', lw=1.1))
    ax.text(8.2, 3210, r'$\mathrm{EA}_1 + \mathrm{EA}_2 = +332$', fontsize=6.5, color='#e65100')

    # Lattice Energy: Gaseous ions -> ZnS(s)
    ax.annotate('', xy=(2.8, -206), xytext=(8.5, 3382), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.5, linestyle='--'))
    ax.text(5.6, 1400, r'$\mathbf{Lattice\ Energy\ (LE)}$' '\n' r'$-3588\ \mathrm{kJ\ mol^{-1}}$', fontsize=7.2, color='#a81717', fontweight='bold', ha='center')

    out_file = os.path.join(fig_dir, "a2_t23_born_haber_zns.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 2: Enthalpy of Solution & Hydration Cycle for KBr (Q18)
# -----------------------------------------------------------------------------
def create_solution_cycle_kbr():
    fig, ax = plt.subplots(figsize=(6.0, 3.0), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(5.0, 7.6, "Enthalpy Cycle for Dissolution of Potassium Bromide, KBr(s)", ha='center', fontsize=9, fontweight='bold', color='#0b1b36')

    # Boxes for states
    # Box 1: KBr(s) (bottom-left)
    ax.text(2.0, 2.0, r'$\mathbf{KBr(s)}$', ha='center', va='center', fontsize=8.5, color='#0b1b36',
            bbox=dict(boxstyle='square,pad=0.5', facecolor='#f1f5f9', edgecolor='#0b1b36', lw=1.2))

    # Box 2: K+(aq) + Br-(aq) (bottom-right)
    ax.text(8.0, 2.0, r'$\mathbf{K^+(aq) + Br^-(aq)}$', ha='center', va='center', fontsize=8.5, color='#0b1b36',
            bbox=dict(boxstyle='square,pad=0.5', facecolor='#f1f5f9', edgecolor='#0b1b36', lw=1.2))

    # Box 3: K+(g) + Br-(g) (top-middle)
    ax.text(5.0, 6.0, r'$\mathbf{K^+(g) + Br^-(g)}$', ha='center', va='center', fontsize=8.5, color='#a81717',
            bbox=dict(boxstyle='square,pad=0.5', facecolor='#fff5f5', edgecolor='#a81717', lw=1.2))

    # Arrows
    # 1. Solution: KBr(s) -> K+(aq) + Br-(aq)
    ax.annotate('', xy=(6.5, 2.0), xytext=(3.0, 2.0), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.5))
    ax.text(4.75, 1.4, r'$\Delta H^\circ_\mathrm{sol} = +19.9\ \mathrm{kJ\ mol^{-1}}$', ha='center', fontsize=7.5, fontweight='bold', color='#a81717')

    # 2. Lattice dissociation: KBr(s) -> K+(g) + Br-(g)
    ax.annotate('', xy=(4.2, 5.5), xytext=(2.4, 2.6), arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.3))
    ax.text(2.5, 4.3, r'$-\mathrm{LE} = +679\ \mathrm{kJ\ mol^{-1}}$' '\n(Lattice dissociation)', ha='center', fontsize=7.0, color='#0b1b36')

    # 3. Hydration: K+(g) + Br-(g) -> K+(aq) + Br-(aq)
    ax.annotate('', xy=(7.4, 2.6), xytext=(5.8, 5.5), arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.3))
    ax.text(7.6, 4.3, r'$\Sigma \Delta H^\circ_\mathrm{hyd} = \Delta H^\circ_\mathrm{hyd}(\mathrm{K^+}) + \Delta H^\circ_\mathrm{hyd}(\mathrm{Br^-})$' '\n' r'$= -322 + (-337) = -659\ \mathrm{kJ\ mol^{-1}}$', ha='center', fontsize=6.8, color='#2e7d32')

    out_file = os.path.join(fig_dir, "a2_t23_solution_cycle_kbr.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 3: Gibbs Free Energy vs Temperature Feasibility Plot (Q28)
# -----------------------------------------------------------------------------
def create_delta_g_temperature_plot():
    fig, ax = plt.subplots(figsize=(6.0, 3.2), dpi=220)
    
    # Range of T: 0 to 800 K
    T = np.linspace(0, 800, 100)
    # Reaction: Endothermic with positive entropy (e.g. CaCO3 or ZnCO3 decomposition)
    # Delta H = +178 kJ/mol, Delta S = +0.160 kJ/(mol K)
    dH = 178.0
    dS = 0.160
    dG = dH - (T * dS)
    
    T_feas = dH / dS  # 1112.5 K -> let's scale so T_feas = 500 K
    dH_scaled = 100.0
    dS_scaled = 0.200
    dG_scaled = dH_scaled - (T * dS_scaled)
    T_crossing = dH_scaled / dS_scaled  # 500 K

    ax.plot(T, dG_scaled, color='#a81717', lw=2.2, label=r'$\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$')
    ax.axhline(0, color='#0b1b36', lw=1.2, linestyle='-')
    ax.axvline(T_crossing, color='#2e7d32', lw=1.2, linestyle='--')

    ax.set_xlim(0, 800)
    ax.set_ylim(-80, 140)
    ax.set_xlabel('Temperature / K', fontsize=8, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'$\Delta G^\circ\ /\ \mathrm{kJ\ mol^{-1}}$', fontsize=8, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Gibbs Free Energy vs Temperature ($\Delta H^\circ > 0,\ \Delta S^\circ > 0$)', fontsize=9, fontweight='bold', color='#0b1b36')

    # Annotations
    ax.plot(0, dH_scaled, 'o', color='#0b1b36', markersize=5)
    ax.text(15, dH_scaled + 5, r'$y\text{-intercept} = \Delta H^\circ\ (+100\ \mathrm{kJ\ mol^{-1}})$', fontsize=7.2, fontweight='bold', color='#0b1b36')

    ax.plot(T_crossing, 0, 's', color='#2e7d32', markersize=6)
    ax.text(T_crossing + 15, 12, r'$T_\mathrm{feas} = \frac{\Delta H^\circ}{\Delta S^\circ} = 500\ \mathrm{K}$' '\n(Reaction becomes feasible)', fontsize=7.2, fontweight='bold', color='#2e7d32')

    # Shaded feasible vs non-feasible regions
    ax.fill_between(T[T >= T_crossing], dG_scaled[T >= T_crossing], 0, color='#2e7d32', alpha=0.15, label='Feasible (ΔG° ≤ 0)')
    ax.fill_between(T[T <= T_crossing], 0, dG_scaled[T <= T_crossing], color='#a81717', alpha=0.10, label='Not Feasible (ΔG° > 0)')

    ax.text(250, 40, r'$\mathbf{Gradient} = -\Delta S^\circ$' '\n(Negative slope)', fontsize=7.2, color='#a81717', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#a81717', lw=0.8))

    ax.legend(frameon=True, facecolor='#f8f9fa', edgecolor='#dcd8d0', fontsize=7.0, loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.5, color='#b0aca4')

    out_file = os.path.join(fig_dir, "a2_t23_delta_g_temperature_plot.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 4: Born-Haber Cycle for BaCl2 (Q41 - HF 1)
# -----------------------------------------------------------------------------
def create_born_haber_bacl2():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(-1300, 2300)
    ax.axis('off')

    # Levels
    # 0: Ba(s) + Cl2(g)
    ax.plot([0.5, 3.0], [0, 0], color='#0b1b36', lw=2.0)
    ax.text(1.75, 55, r'$\mathrm{Ba(s)} + \mathrm{Cl_2(g)}$', ha='center', fontsize=7.5, fontweight='bold', color='#0b1b36')

    # -1: BaCl2(s)
    ax.plot([0.5, 3.0], [-859, -859], color='#a81717', lw=2.0)
    ax.text(1.75, -950, r'$\mathrm{BaCl_2(s)}$', ha='center', fontsize=7.5, fontweight='bold', color='#a81717')

    # 1: Ba(g) + Cl2(g)
    ax.plot([3.4, 5.4], [180, 180], color='#0b1b36', lw=1.8)
    ax.text(4.4, 235, r'$\mathrm{Ba(g)} + \mathrm{Cl_2(g)}$', ha='center', fontsize=7.0, color='#0b1b36')

    # 2: Ba(g) + 2Cl(g)
    ax.plot([3.4, 5.4], [422, 422], color='#0b1b36', lw=1.8)
    ax.text(4.4, 475, r'$\mathrm{Ba(g)} + 2\mathrm{Cl(g)}$', ha='center', fontsize=7.0, color='#0b1b36')

    # 3: Ba2+(g) + 2Cl(g) + 2e-
    ax.plot([5.8, 8.2], [1890, 1890], color='#0b1b36', lw=1.8)
    ax.text(7.0, 1950, r'$\mathrm{Ba^{2+}(g)} + 2\mathrm{Cl(g)} + 2\mathrm{e^-}$', ha='center', fontsize=7.0, color='#0b1b36')

    # 4: Ba2+(g) + 2Cl-(g)
    ax.plot([6.8, 9.5], [1192, 1192], color='#0b1b36', lw=2.0)
    ax.text(8.15, 1250, r'$\mathrm{Ba^{2+}(g)} + 2\mathrm{Cl^-(g)}$', ha='center', fontsize=7.5, fontweight='bold', color='#0b1b36')

    # Arrows
    # Formation: 0 -> -859
    ax.annotate('', xy=(1.0, -859), xytext=(1.0, 0), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.3))
    ax.text(0.2, -430, r'$\Delta H^\circ_\mathrm{f} = -859$', fontsize=6.8, color='#a81717', fontweight='bold', va='center')

    # Atomisation Ba
    ax.annotate('', xy=(3.5, 180), xytext=(3.0, 0), arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.1))
    ax.text(3.3, 70, r'$+180$', fontsize=6.5, color='#2e7d32')

    # Dissociation Cl2: BE(Cl2) = +242
    ax.annotate('', xy=(4.5, 422), xytext=(4.5, 180), arrowprops=dict(arrowstyle='->', color='#2e7d32', lw=1.1))
    ax.text(4.6, 290, r'$+242$', fontsize=6.5, color='#2e7d32')

    # Ionisation Ba (IE1 + IE2 = 503 + 965 = +1468)
    ax.annotate('', xy=(6.5, 1890), xytext=(5.5, 422), arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.1))
    ax.text(5.5, 1100, r'$\mathrm{IE}_1 + \mathrm{IE}_2 = +1468$', fontsize=6.5, color='#1565c0', rotation=60)

    # Electron affinity 2 x Cl = 2 x (-349) = -698
    ax.annotate('', xy=(8.2, 1192), xytext=(8.2, 1890), arrowprops=dict(arrowstyle='->', color='#e65100', lw=1.3))
    ax.text(8.3, 1540, r'$2\times\mathrm{EA} = -698$', fontsize=6.5, color='#e65100')

    # Lattice Energy: Gaseous ions -> BaCl2(s)
    ax.annotate('', xy=(2.8, -859), xytext=(8.5, 1192), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.5, linestyle='--'))
    ax.text(5.5, 100, r'$\mathbf{Lattice\ Energy\ (LE)}$' '\n' r'$-2051\ \mathrm{kJ\ mol^{-1}}$', fontsize=7.2, color='#a81717', fontweight='bold', ha='center')

    out_file = os.path.join(fig_dir, "a2_t23_born_haber_bacl2.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 5: Group 2 Sulfate Solubility Rationale Trend (Q44 - HF 4)
# -----------------------------------------------------------------------------
def create_group2_enthalpy_trend():
    fig, ax = plt.subplots(figsize=(6.0, 3.0), dpi=220)

    cations = ['Mg2+', 'Ca2+', 'Sr2+', 'Ba2+']
    r_cat = [0.072, 0.100, 0.118, 0.135] # nm
    # Magnitudes in kJ/mol
    hyd_magnitude = [1920, 1650, 1480, 1360]  # steep decline
    le_magnitude = [2900, 2700, 2550, 2450]   # shallow decline
    # Delta H sol = Hyd - LE (approx relative values)
    dH_sol = [-90, -18, +20, +45] # becomes more endothermic

    x = np.arange(len(cations))
    width = 0.35

    ax.plot(x, hyd_magnitude, 'o-', color='#1565c0', lw=2.0, markersize=6, label=r'Cation Hydration Magnitude $|\Delta H^\circ_\mathrm{hyd}|$ (Steep drop)')
    ax.plot(x, le_magnitude, 's-', color='#a81717', lw=2.0, markersize=6, label=r'Lattice Energy Magnitude $|\mathrm{LE}|$ (Gentle drop)')

    ax.set_xticks(x)
    ax.set_xticklabels([r'$\mathrm{Mg^{2+}}$' '\n(Small radius)', r'$\mathrm{Ca^{2+}}$', r'$\mathrm{Sr^{2+}}$', r'$\mathrm{Ba^{2+}}$' '\n(Large radius)'], fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'Enthalpy Magnitude / $\mathrm{kJ\ mol^{-1}}$', fontsize=8, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Why Group 2 Sulfate Solubility Decreases: Relative Rates of Change', fontsize=8.8, fontweight='bold', color='#0b1b36')
    ax.set_ylim(1100, 3200)

    # Annotations
    ax.annotate(r'$|\Delta H^\circ_\mathrm{hyd}|$ falls rapidly' '\n' r'($\propto 1/r_+$)', xy=(0, 1920), xytext=(0.2, 2200),
                arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.0), fontsize=6.8, color='#1565c0', fontweight='bold')

    ax.annotate(r'$|\mathrm{LE}|$ falls slowly' '\n' r'($\mathrm{SO_4^{2-}}$ is large, $r_+ + r_-$ changes little)', xy=(3, 2450), xytext=(1.6, 2800),
                arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.0), fontsize=6.8, color='#a81717', fontweight='bold')

    ax.legend(frameon=True, facecolor='#f8f9fa', edgecolor='#dcd8d0', fontsize=7.0, loc='lower left')
    ax.grid(True, linestyle=':', alpha=0.5, color='#b0aca4')

    out_file = os.path.join(fig_dir, "a2_t23_group2_enthalpy_trend.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_born_haber_zns()
    create_solution_cycle_kbr()
    create_delta_g_temperature_plot()
    create_born_haber_bacl2()
    create_group2_enthalpy_trend()
    print("All Topic 23 figures successfully generated.")
