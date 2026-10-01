"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for Topic 26: Reaction Kinetics
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
# Figure 1: Arrhenius Plot (ln k vs 1/T)
# -----------------------------------------------------------------------------
def create_arrhenius_plot():
    fig, ax = plt.subplots(figsize=(6.0, 3.2), dpi=220)

    # 1/T from 0.0030 to 0.0035 K^-1 (approx 285 K to 333 K)
    inv_T = np.array([3.00, 3.10, 3.20, 3.30, 3.40, 3.50]) # in 10^-3 K^-1
    # ln k = ln A - (Ea/R)*(1/T). Let Ea = 75 kJ/mol, R = 8.314 J/mol K => Ea/R = 9021 K
    # ln k = 22.0 - 9.021 * inv_T
    ln_k = 22.0 - 9.021 * inv_T

    ax.plot(inv_T, ln_k, 'o-', color='#a81717', lw=1.8, markersize=5, markerfacecolor='#1565c0', label=r'$\mathrm{Experimental\ Data}$')
    
    # Mark gradient triangle
    ax.plot([3.10, 3.40], [-5.965, -5.965], '--', color='#555555', lw=0.9)
    ax.plot([3.40, 3.40], [-5.965, -8.671], '--', color='#555555', lw=0.9)
    ax.text(3.25, -5.6, r'$\Delta(1/T) = 0.30 \times 10^{-3}\ \mathrm{K^{-1}}$', fontsize=6.8, ha='center', color='#555555')
    ax.text(3.43, -7.3, r'$\Delta(\ln k) = -2.71$', fontsize=6.8, ha='left', color='#555555')

    ax.annotate(r'$\mathbf{Gradient} = -\frac{E_\mathrm{a}}{R}$' '\n' r'${E_\mathrm{a}} = -R \times \mathrm{gradient}$',
                xy=(3.25, -7.3), xytext=(3.05, -8.5),
                arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.0),
                fontsize=7.5, color='#0b1b36', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#0b1b36', lw=0.8))

    ax.set_xlabel(r'$(1/T)\ /\ 10^{-3}\ \mathrm{K^{-1}}$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'$\ln\ (k\ /\ \mathrm{mol^{-1}\ dm^3\ s^{-1}})$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Arrhenius Plot of $\ln k$ against $1/T$ for the Decomposition of $\mathrm{N_2O_5}$', fontsize=8.5, fontweight='bold', color='#0b1b36')

    ax.grid(True, linestyle=':', alpha=0.5, color='#b0aca4')
    ax.legend(frameon=True, facecolor='#f8f9fa', edgecolor='#dcd8d0', fontsize=7.0, loc='upper right')

    out_file = os.path.join(fig_dir, "a2_t26_arrhenius_plot.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 2: Rate vs Concentration Graphs for 0th, 1st, and 2nd Order
# -----------------------------------------------------------------------------
def create_rate_conc_graphs():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(6.5, 2.5), dpi=220)

    conc = np.linspace(0, 1.0, 100)

    # Zero order: Rate = k
    ax1.plot(conc, np.ones_like(conc) * 0.5, color='#a81717', lw=2.0)
    ax1.set_title('Zero Order\n' r'$\mathrm{Rate} = k[\mathrm{A}]^0$', fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax1.set_xlabel(r'$[\mathrm{A}]\ /\ \mathrm{mol\ dm^{-3}}$', fontsize=6.8, fontweight='bold', color='#0b1b36')
    ax1.set_ylabel(r'$\mathrm{Rate}\ /\ \mathrm{mol\ dm^{-3}\ s^{-1}}$', fontsize=6.8, fontweight='bold', color='#0b1b36')
    ax1.set_ylim(0, 1.0)
    ax1.set_xlim(0, 1.0)
    ax1.grid(True, linestyle=':', alpha=0.4)

    # First order: Rate = k[A]
    ax2.plot(conc, 0.8 * conc, color='#1565c0', lw=2.0)
    ax2.set_title('First Order\n' r'$\mathrm{Rate} = k[\mathrm{A}]^1$', fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax2.set_xlabel(r'$[\mathrm{A}]\ /\ \mathrm{mol\ dm^{-3}}$', fontsize=6.8, fontweight='bold', color='#0b1b36')
    ax2.set_ylim(0, 1.0)
    ax2.set_xlim(0, 1.0)
    ax2.grid(True, linestyle=':', alpha=0.4)

    # Second order: Rate = k[A]^2
    ax3.plot(conc, 0.9 * (conc**2), color='#2e7d32', lw=2.0)
    ax3.set_title('Second Order\n' r'$\mathrm{Rate} = k[\mathrm{A}]^2$', fontsize=7.5, fontweight='bold', color='#0b1b36')
    ax3.set_xlabel(r'$[\mathrm{A}]\ /\ \mathrm{mol\ dm^{-3}}$', fontsize=6.8, fontweight='bold', color='#0b1b36')
    ax3.set_ylim(0, 1.0)
    ax3.set_xlim(0, 1.0)
    ax3.grid(True, linestyle=':', alpha=0.4)

    out_file = os.path.join(fig_dir, "a2_t26_rate_conc_orders.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 3: Concentration vs Time Curve with Successive Half-Lives (First Order)
# -----------------------------------------------------------------------------
def create_first_order_half_life():
    fig, ax = plt.subplots(figsize=(6.0, 3.2), dpi=220)

    t = np.linspace(0, 200, 200)
    # k = ln(2)/50 = 0.01386 s^-1, t1/2 = 50 s
    k = np.log(2) / 50.0
    conc = 1.0 * np.exp(-k * t)

    ax.plot(t, conc, color='#a81717', lw=2.2, label=r'$[\mathrm{A}]_t = [\mathrm{A}]_0 e^{-kt}$')

    # Half-life points
    t_halves = [50, 100, 150]
    c_halves = [0.50, 0.25, 0.125]

    for i, (th, ch) in enumerate(zip(t_halves, c_halves)):
        ax.plot(th, ch, 'o', color='#1565c0', markersize=5)
        ax.axvline(th, color='#1565c0', linestyle=':', lw=0.9)
        ax.axhline(ch, color='#1565c0', linestyle=':', lw=0.9)

    ax.annotate(r'$t_{1/2} = 50\ \mathrm{s}$', xy=(25, 0.52), fontsize=7.2, color='#1565c0', fontweight='bold', ha='center')
    ax.annotate(r'$t_{1/2} = 50\ \mathrm{s}$', xy=(75, 0.27), fontsize=7.2, color='#1565c0', fontweight='bold', ha='center')
    ax.annotate(r'$t_{1/2} = 50\ \mathrm{s}$', xy=(125, 0.145), fontsize=7.2, color='#1565c0', fontweight='bold', ha='center')

    ax.text(120, 0.75, r'$\mathbf{First\text{-}Order\ Characteristic:}$' '\n' r'Constant half-life, $t_{1/2} = \frac{\ln 2}{k}$' '\n' r'Independent of initial concentration',
            fontsize=7.2, color='#0b1b36', bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#0b1b36', lw=0.8))

    ax.set_xlim(0, 200)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel(r'Time / $\mathrm{s}$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'Concentration / $\mathrm{mol\ dm^{-3}}$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Concentration–Time Decay for First-Order Reaction Showing Constant $t_{1/2}$', fontsize=8.5, fontweight='bold', color='#0b1b36')

    ax.grid(True, linestyle=':', alpha=0.5, color='#b0aca4')

    out_file = os.path.join(fig_dir, "a2_t26_first_order_half_life.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 4: Multistep Reaction Profile Showing Rate-Determining Step
# -----------------------------------------------------------------------------
def create_multistep_energy_profile():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)

    # 2-step profile: Reactants -> TS1 (high, RDS) -> Intermediate -> TS2 (lower) -> Products
    x = np.linspace(0, 10, 300)
    # Piecewise or smooth curve
    # Reactants: (1, 20)
    # TS1: (3.5, 85) - high barrier Ea1 = 65 kJ
    # Interm: (5.5, 45)
    # TS2: (7.5, 65) - lower barrier Ea2 = 20 kJ from intermediate
    # Products: (9.5, 10) - exothermic overall
    y = (20 + 65 * np.exp(-((x - 3.5)/0.9)**2) 
            + 25 * np.exp(-((x - 5.5)/0.8)**2) 
            + 45 * np.exp(-((x - 7.5)/0.9)**2) 
            - 10 * (1 / (1 + np.exp(-2*(x - 5)))))

    # Normalize roughly
    ax.plot(x, y, color='#a81717', lw=2.2)

    # Annotations
    ax.text(0.8, 22, r'$\mathbf{Reactants}$' '\n' r'$\mathrm{A + B}$', fontsize=7.2, fontweight='bold', color='#0b1b36')
    ax.text(3.5, 90, r'$\mathbf{Transition\ State\ 1\ (TS_1)}$' '\n' r'(Rate-Determining Step)', fontsize=7.0, ha='center', color='#c2185b', fontweight='bold')
    ax.text(5.5, 48, r'$\mathbf{Intermediate}$' '\n' r'$\mathrm{I}$', fontsize=7.0, ha='center', color='#1565c0', fontweight='bold')
    ax.text(7.5, 78, r'$\mathbf{Transition\ State\ 2\ (TS_2)}$', fontsize=7.0, ha='center', color='#2e7d32', fontweight='bold')
    ax.text(9.2, 12, r'$\mathbf{Products}$' '\n' r'$\mathrm{C + D}$', fontsize=7.2, fontweight='bold', color='#0b1b36')

    # Ea1 arrow
    ax.annotate('', xy=(3.5, 87), xytext=(3.5, 20), arrowprops=dict(arrowstyle='<->', color='#c2185b', lw=1.2))
    ax.text(3.6, 53, r'$E_{\mathrm{a},1}\ (\mathrm{RDS})$', fontsize=7.0, color='#c2185b', fontweight='bold')

    # Delta H arrow
    ax.annotate('', xy=(9.7, 10), xytext=(9.7, 20), arrowprops=dict(arrowstyle='<->', color='#0b1b36', lw=1.0))
    ax.text(9.8, 15, r'$\Delta H < 0$', fontsize=7.0, color='#0b1b36', fontweight='bold')

    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 100)
    ax.set_xlabel(r'Reaction Coordinate', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'Potential Energy / $\mathrm{kJ\ mol^{-1}}$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Two-Step Reaction Potential Energy Profile Showing Rate-Determining Step', fontsize=8.5, fontweight='bold', color='#0b1b36')

    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)

    out_file = os.path.join(fig_dir, "a2_t26_multistep_energy_profile.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 5: Continuous Monitoring: Absorbance vs Time for Iodine Reaction
# -----------------------------------------------------------------------------
def create_continuous_monitoring_graph():
    fig, ax = plt.subplots(figsize=(6.0, 3.2), dpi=220)

    # Propanone + Iodine in acid: zero order with respect to I2, so absorbance drops linearly!
    t = np.linspace(0, 120, 100)
    abs_val = 1.0 - 0.0075 * t # linear decrease

    ax.plot(t, abs_val, color='#a81717', lw=2.2, label=r'$\mathrm{Absorbance\ of\ I_2\ (at\ 450\ nm)}$')
    
    # Tangent / slope
    ax.annotate(r'$\mathbf{Constant\ Slope} = -\mathrm{Rate}$' '\n' r'Zero order with respect to $\mathrm{I_2}$' '\n' r'Rate does not depend on $[\mathrm{I_2}]$',
                xy=(60, 0.55), xytext=(65, 0.75),
                arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.0),
                fontsize=7.2, color='#1565c0', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#1565c0', lw=0.8))

    ax.set_xlim(0, 120)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel(r'Time / $\mathrm{s}$', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_ylabel(r'Absorbance / arbitrary units', fontsize=8.0, fontweight='bold', color='#0b1b36')
    ax.set_title(r'Colorimetric Monitoring of $\mathrm{CH_3COCH_3 + I_2 \rightarrow CH_3COCH_2I + HI}$', fontsize=8.5, fontweight='bold', color='#0b1b36')

    ax.grid(True, linestyle=':', alpha=0.5, color='#b0aca4')
    ax.legend(frameon=True, facecolor='#f8f9fa', edgecolor='#dcd8d0', fontsize=7.0, loc='lower left')

    out_file = os.path.join(fig_dir, "a2_t26_colorimetry_absorbance.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_arrhenius_plot()
    create_rate_conc_graphs()
    create_first_order_half_life()
    create_multistep_energy_profile()
    create_continuous_monitoring_graph()
    print("All Topic 26 figures successfully generated.")
