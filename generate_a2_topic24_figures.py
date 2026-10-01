"""
Generate High-Quality Cambridge 9701 Paper 4 Figures for Topic 24: Electrochemistry
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
# Figure 1: Standard Hydrogen Electrode (SHE) (Q4 / HF Q41)
# -----------------------------------------------------------------------------
def create_she_apparatus():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Beaker
    ax.plot([2.5, 2.5, 7.5, 7.5], [7.0, 1.5, 1.5, 7.0], color='#0b1b36', lw=2.0)
    # Solution level
    ax.plot([2.5, 7.5], [5.0, 5.0], color='#1565c0', lw=1.2, linestyle='--')
    ax.fill_between([2.5, 7.5], 1.5, 5.0, color='#1565c0', alpha=0.10)
    ax.text(6.8, 2.5, r'$1.00\ \mathrm{mol\ dm^{-3}}\ \mathrm{H^+(aq)}$' '\n' r'$(298\ \mathrm{K})$', fontsize=7.2, color='#1565c0', ha='center', fontweight='bold')

    # Glass tube for H2 inlet
    # Outer tube
    ax.plot([4.2, 4.2, 4.0, 4.0], [9.5, 4.0, 4.0, 3.2], color='#0b1b36', lw=1.5)
    ax.plot([5.8, 5.8, 6.0, 6.0], [9.5, 4.0, 4.0, 3.2], color='#0b1b36', lw=1.5)
    # Side arm / gas inlet
    ax.plot([3.0, 4.2], [8.5, 8.5], color='#0b1b36', lw=1.5)
    ax.plot([3.0, 4.2], [9.0, 9.0], color='#0b1b36', lw=1.5)
    ax.annotate('', xy=(3.8, 8.75), xytext=(2.6, 8.75), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.5))
    ax.text(2.4, 9.0, r'$\mathbf{H_2(g)\ in}$' '\n' r'$1.00\ \mathrm{bar}\ (100\ \mathrm{kPa})$' '\n' r'$298\ \mathrm{K}$', fontsize=6.8, color='#a81717', ha='right', fontweight='bold')

    # Platinum wire inside
    ax.plot([5.0, 5.0], [9.8, 2.3], color='#37474f', lw=1.2)
    # Platinum foil / plate
    ax.fill_between([4.6, 5.4], 2.0, 2.6, color='#263238')
    ax.plot([4.6, 5.4, 5.4, 4.6, 4.6], [2.0, 2.0, 2.6, 2.6, 2.0], color='#000000', lw=1.2)
    ax.text(5.0, 1.7, 'Platinised Pt foil', fontsize=6.8, color='#0b1b36', ha='center', fontweight='bold')

    # Wire to external circuit
    ax.plot([5.0, 5.0], [9.8, 10.0], color='#d32f2f', lw=1.5)
    ax.plot(5.0, 10.0, 'o', color='#d32f2f', markersize=4)
    ax.text(5.0, 10.2, 'Connection to circuit (Pt wire)', fontsize=6.8, color='#d32f2f', ha='center', fontweight='bold')

    # Escaping bubbles
    for bx, by in [(4.3, 3.6), (4.1, 4.2), (5.9, 3.5), (6.1, 4.4), (5.7, 4.8)]:
        circle = plt.Circle((bx, by), 0.12, color='#1565c0', fill=False, lw=1.0)
        ax.add_patch(circle)
    ax.text(4.2, 5.5, 'Escaping $\mathrm{H_2(g)}$ bubbles', fontsize=6.2, color='#1565c0', fontstyle='italic')

    # Reaction equation box
    ax.text(5.0, 0.4, r'$\mathbf{2H^+(aq) + 2e^- \rightleftharpoons H_2(g)}\quad (E^\circ = 0.00\ \mathrm{V})$', fontsize=7.5, color='#0b1b36', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fa', edgecolor='#0b1b36', lw=0.8))

    out_file = os.path.join(fig_dir, "a2_t24_she_apparatus.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 2: Standard Electrochemical Cell (Zn/Zn2+ || Cu2+/Cu) (Q2 / Q42)
# -----------------------------------------------------------------------------
def create_electrochemical_cell():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Beaker 1 (Left: Zn)
    ax.plot([1.0, 1.0, 4.5, 4.5], [6.5, 1.5, 1.5, 6.5], color='#0b1b36', lw=1.8)
    ax.plot([1.0, 4.5], [5.0, 5.0], color='#546e7a', lw=1.0, linestyle='--')
    ax.fill_between([1.0, 4.5], 1.5, 5.0, color='#eceff1', alpha=0.6)
    ax.text(2.75, 2.5, r'$1.00\ \mathrm{mol\ dm^{-3}}\ \mathrm{Zn^{2+}(aq)}$', fontsize=6.8, color='#0b1b36', ha='center', fontweight='bold')

    # Electrode 1 (Zn rod)
    ax.fill_between([2.2, 2.6], 3.0, 7.5, color='#90a4ae')
    ax.plot([2.2, 2.6, 2.6, 2.2, 2.2], [3.0, 3.0, 7.5, 7.5, 3.0], color='#37474f', lw=1.0)
    ax.text(2.4, 8.0, r'$\mathbf{Zn(s)\ Anode}$' '\n' r'$(E^\circ = -0.76\ \mathrm{V})$', fontsize=6.8, color='#0b1b36', ha='center', fontweight='bold')

    # Beaker 2 (Right: Cu)
    ax.plot([7.5, 7.5, 11.0, 11.0], [6.5, 1.5, 1.5, 6.5], color='#0b1b36', lw=1.8)
    ax.plot([7.5, 11.0], [5.0, 5.0], color='#1565c0', lw=1.0, linestyle='--')
    ax.fill_between([7.5, 11.0], 1.5, 5.0, color='#1565c0', alpha=0.15)
    ax.text(9.25, 2.5, r'$1.00\ \mathrm{mol\ dm^{-3}}\ \mathrm{Cu^{2+}(aq)}$', fontsize=6.8, color='#1565c0', ha='center', fontweight='bold')

    # Electrode 2 (Cu rod)
    ax.fill_between([9.4, 9.8], 3.0, 7.5, color='#bcaaa4')
    ax.plot([9.4, 9.8, 9.8, 9.4, 9.4], [3.0, 3.0, 7.5, 7.5, 3.0], color='#5d4037', lw=1.0)
    ax.text(9.6, 8.0, r'$\mathbf{Cu(s)\ Cathode}$' '\n' r'$(E^\circ = +0.34\ \mathrm{V})$', fontsize=6.8, color='#a81717', ha='center', fontweight='bold')

    # Salt Bridge (inverted U-tube)
    ax.plot([3.5, 3.5, 4.0, 4.0], [3.5, 6.8, 6.8, 3.5], color='#2e7d32', lw=1.2)
    ax.plot([8.0, 8.0, 8.5, 8.5], [3.5, 6.8, 6.8, 3.5], color='#2e7d32', lw=1.2)
    ax.plot([3.5, 8.5], [6.8, 6.8], color='#2e7d32', lw=1.2)
    ax.plot([4.0, 8.0], [6.4, 6.4], color='#2e7d32', lw=1.2)
    ax.fill_between([3.5, 4.0], 3.5, 6.4, color='#a5d6a7', alpha=0.6)
    ax.fill_between([8.0, 8.5], 3.5, 6.4, color='#a5d6a7', alpha=0.6)
    ax.fill_between([4.0, 8.0], 6.4, 6.8, color='#a5d6a7', alpha=0.6)
    ax.text(6.0, 7.1, r'$\mathbf{Salt\ Bridge}$' '\n' r'(Filter paper soaked in saturated $\mathrm{KNO_3(aq)}$)', fontsize=6.5, color='#2e7d32', ha='center', fontweight='bold')

    # External Circuit & Voltmeter
    ax.plot([2.4, 2.4, 5.4], [7.5, 9.2, 9.2], color='#0b1b36', lw=1.4)
    ax.plot([6.6, 9.6, 9.6], [9.2, 9.2, 7.5], color='#0b1b36', lw=1.4)

    # Voltmeter circle
    circle = plt.Circle((6.0, 9.2), 0.6, color='#0b1b36', fill=True, facecolor='#ffffff', lw=1.5)
    ax.add_patch(circle)
    ax.text(6.0, 9.05, r'$\mathbf{V}$', fontsize=9.0, color='#0b1b36', ha='center', va='center', fontweight='bold')
    ax.text(6.0, 9.9, r'$E^\circ_\mathrm{cell} = +1.10\ \mathrm{V}$', fontsize=7.5, color='#a81717', ha='center', fontweight='bold')

    # Electron flow arrow
    ax.annotate('', xy=(8.2, 9.4), xytext=(3.8, 9.4), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.5))
    ax.text(6.0, 8.5, r'Electron Flow ($\mathrm{e^-}$): $\mathrm{Zn \rightarrow Cu}$', fontsize=6.8, color='#a81717', ha='center', fontweight='bold')

    # Cell notation at bottom
    ax.text(6.0, 0.4, r'$\mathbf{Zn(s)\ |\ Zn^{2+}(aq, 1.0\ M)\ ||\ Cu^{2+}(aq, 1.0\ M)\ |\ Cu(s)}$', fontsize=7.2, color='#0b1b36', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fa', edgecolor='#dcd8d0', lw=0.8))

    out_file = os.path.join(fig_dir, "a2_t24_electrochemical_cell.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 3: Quantitative Electrolysis Apparatus (Q1 / Q17)
# -----------------------------------------------------------------------------
def create_electrolysis_coulometer():
    fig, ax = plt.subplots(figsize=(6.2, 3.0), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Beaker / Electrolytic Cell
    ax.plot([2.0, 2.0, 8.0, 8.0], [7.0, 1.5, 1.5, 7.0], color='#0b1b36', lw=2.0)
    ax.plot([2.0, 8.0], [5.5, 5.5], color='#1565c0', lw=1.0, linestyle='--')
    ax.fill_between([2.0, 8.0], 1.5, 5.5, color='#1565c0', alpha=0.15)
    ax.text(5.0, 2.0, r'Aqueous copper(II) sulfate, $\mathrm{CuSO_4(aq)}$', fontsize=7.0, color='#1565c0', ha='center', fontweight='bold')

    # Cathode (negative, Cu deposition)
    ax.fill_between([3.2, 3.6], 2.8, 7.8, color='#bcaaa4')
    ax.plot([3.2, 3.6, 3.6, 3.2, 3.2], [2.8, 2.8, 7.8, 7.8, 2.8], color='#5d4037', lw=1.2)
    ax.text(3.4, 8.2, r'$\mathbf{Cathode\ (-)}$' '\n' r'Pure Cu plate (gains mass)', fontsize=6.5, color='#a81717', ha='center', fontweight='bold')

    # Anode (positive, impure or pure Cu dissolution)
    ax.fill_between([6.4, 6.8], 2.8, 7.8, color='#bcaaa4')
    ax.plot([6.4, 6.8, 6.8, 6.4, 6.4], [2.8, 2.8, 7.8, 7.8, 2.8], color='#5d4037', lw=1.2)
    ax.text(6.6, 8.2, r'$\mathbf{Anode\ (+)}$' '\n' r'Cu plate (loses mass)', fontsize=6.5, color='#0b1b36', ha='center', fontweight='bold')

    # External Circuit: Power supply, Variable resistor, Ammeter
    # Left lead from Cathode up to power supply
    ax.plot([3.4, 3.4, 4.4], [7.8, 9.4, 9.4], color='#0b1b36', lw=1.3)
    # DC Power Supply symbol
    ax.plot([4.4, 4.4], [9.1, 9.7], color='#0b1b36', lw=2.5) # positive long
    ax.plot([4.7, 4.7], [9.25, 9.55], color='#0b1b36', lw=3.5) # negative short
    ax.text(4.4, 9.85, '+', fontsize=8.0, fontweight='bold', ha='center')
    ax.text(4.7, 9.85, '−', fontsize=8.0, fontweight='bold', ha='center')

    # Variable resistor
    ax.plot([4.7, 5.6], [9.4, 9.4], color='#0b1b36', lw=1.3)
    ax.plot([5.6, 6.4, 6.4, 5.6, 5.6], [9.2, 9.2, 9.6, 9.6, 9.2], color='#0b1b36', lw=1.0)
    ax.plot([5.5, 6.5], [9.0, 9.8], color='#a81717', lw=1.2) # arrow across rheostat
    ax.text(6.0, 10.0, 'Rheostat (constant current)', fontsize=6.2, color='#0b1b36', ha='center')

    # Ammeter
    ax.plot([6.4, 7.4], [9.4, 9.4], color='#0b1b36', lw=1.3)
    circle = plt.Circle((7.8, 9.4), 0.4, color='#0b1b36', fill=True, facecolor='#ffffff', lw=1.2)
    ax.add_patch(circle)
    ax.text(7.8, 9.35, r'$\mathbf{A}$', fontsize=8.0, color='#0b1b36', ha='center', va='center', fontweight='bold')

    # Lead down to Anode
    ax.plot([8.2, 6.6, 6.6], [9.4, 9.4, 7.8], color='#0b1b36', lw=1.3)

    # Faraday equation box
    ax.text(5.0, 0.4, r'$\mathbf{Q = I \times t}\quad \mathrm{and}\quad \mathbf{n(e^-) = \frac{Q}{F} = \frac{I \times t}{Le}}\quad (\mathrm{Cu^{2+} + 2e^- \rightarrow Cu})$',
            fontsize=7.2, color='#0b1b36', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fa', edgecolor='#0b1b36', lw=0.8))

    out_file = os.path.join(fig_dir, "a2_t24_electrolysis_coulometer.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 4: Alkaline Hydrogen-Oxygen Fuel Cell (Q5 / Q43)
# -----------------------------------------------------------------------------
def create_alkaline_fuel_cell():
    fig, ax = plt.subplots(figsize=(6.2, 3.2), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Main outer chamber
    ax.plot([2.0, 2.0, 8.0, 8.0, 2.0], [2.0, 8.0, 8.0, 2.0, 2.0], color='#0b1b36', lw=2.0)

    # Porous Anode (left)
    ax.fill_between([3.2, 3.8], 2.0, 8.0, color='#90a4ae', alpha=0.8)
    ax.plot([3.2, 3.2], [2.0, 8.0], color='#37474f', lw=1.5, linestyle=':')
    ax.plot([3.8, 3.8], [2.0, 8.0], color='#37474f', lw=1.5, linestyle=':')
    ax.text(3.5, 8.3, r'$\mathbf{Anode\ (-)}$' '\n(Porous Pt/C)', fontsize=6.8, color='#0b1b36', ha='center', fontweight='bold')

    # Porous Cathode (right)
    ax.fill_between([6.2, 6.8], 2.0, 8.0, color='#90a4ae', alpha=0.8)
    ax.plot([6.2, 6.2], [2.0, 8.0], color='#37474f', lw=1.5, linestyle=':')
    ax.plot([6.8, 6.8], [2.0, 8.0], color='#37474f', lw=1.5, linestyle=':')
    ax.text(6.5, 8.3, r'$\mathbf{Cathode\ (+)}$' '\n(Porous Pt/C)', fontsize=6.8, color='#a81717', ha='center', fontweight='bold')

    # Electrolyte compartment (center)
    ax.fill_between([3.8, 6.2], 2.0, 8.0, color='#fff9c4', alpha=0.5)
    ax.text(5.0, 5.0, r'$\mathbf{Hot\ Aqueous\ KOH}$' '\n' r'$\mathbf{Electrolyte}$' '\n' r'($\mathrm{OH^-}$ ion flow)', fontsize=7.2, color='#f57f17', ha='center', fontweight='bold')
    # OH- migration arrow from cathode to anode
    ax.annotate('', xy=(4.0, 3.5), xytext=(6.0, 3.5), arrowprops=dict(arrowstyle='->', color='#f57f17', lw=1.5))
    ax.text(5.0, 3.8, r'$\mathrm{OH^-}$ ions', fontsize=6.5, color='#f57f17', ha='center', fontweight='bold')

    # Inlets & Outlets
    # H2 In (top left)
    ax.annotate('', xy=(2.0, 6.8), xytext=(0.8, 6.8), arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.5))
    ax.text(0.7, 6.8, r'$\mathbf{H_2(g)\ in}$', fontsize=7.0, color='#1565c0', ha='right', va='center', fontweight='bold')

    # Excess H2 / H2O out (bottom left)
    ax.annotate('', xy=(0.8, 3.2), xytext=(2.0, 3.2), arrowprops=dict(arrowstyle='->', color='#546e7a', lw=1.5))
    ax.text(0.7, 3.2, r'Excess $\mathrm{H_2}$ & $\mathrm{H_2O}$ out', fontsize=6.5, color='#546e7a', ha='right', va='center')

    # O2 In (top right)
    ax.annotate('', xy=(8.0, 6.8), xytext=(9.2, 6.8), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.5))
    ax.text(9.3, 6.8, r'$\mathbf{O_2(g)\ in}$', fontsize=7.0, color='#a81717', ha='left', va='center', fontweight='bold')

    # Unreacted O2 out (bottom right)
    ax.annotate('', xy=(9.2, 3.2), xytext=(8.0, 3.2), arrowprops=dict(arrowstyle='->', color='#546e7a', lw=1.5))
    ax.text(9.3, 3.2, r'Unreacted $\mathrm{O_2}$ out', fontsize=6.5, color='#546e7a', ha='left', va='center')

    # External Circuit
    ax.plot([3.5, 3.5, 4.5], [8.0, 9.4, 9.4], color='#0b1b36', lw=1.3)
    ax.plot([5.5, 6.5, 6.5], [9.4, 9.4, 8.0], color='#0b1b36', lw=1.3)
    # Load / Motor
    circle = plt.Circle((5.0, 9.4), 0.5, color='#0b1b36', fill=True, facecolor='#ffffff', lw=1.3)
    ax.add_patch(circle)
    ax.text(5.0, 9.35, r'$\mathbf{Load}$', fontsize=7.0, color='#0b1b36', ha='center', va='center', fontweight='bold')
    # Electron arrow
    ax.annotate('', xy=(4.5, 9.6), xytext=(3.7, 9.6), arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.2))
    ax.text(4.1, 9.9, r'$\mathrm{e^-}$', fontsize=7.0, color='#a81717', fontweight='bold')

    # Overall Reaction Box
    ax.text(5.0, 0.6, r'$\mathbf{Anode:\ 2H_2 + 4OH^- \rightarrow 4H_2O + 4e^-}\quad\mathbf{Cathode:\ O_2 + 2H_2O + 4e^- \rightarrow 4OH^-}$' '\n' r'$\mathbf{Overall:\ 2H_2(g) + O_2(g) \rightarrow 2H_2O(l)}\quad (E^\circ_\mathrm{cell} = +1.23\ \mathrm{V})$',
            fontsize=6.5, color='#0b1b36', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fa', edgecolor='#0b1b36', lw=0.8))

    out_file = os.path.join(fig_dir, "a2_t24_alkaline_fuel_cell.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

# -----------------------------------------------------------------------------
# Figure 5: Copper Concentration Cell (Q10 / Q45)
# -----------------------------------------------------------------------------
def create_concentration_cell():
    fig, ax = plt.subplots(figsize=(6.2, 3.0), dpi=220)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Left beaker: Dilute Cu2+ (0.010 mol dm-3)
    ax.plot([1.0, 1.0, 4.5, 4.5], [6.5, 1.5, 1.5, 6.5], color='#0b1b36', lw=1.8)
    ax.plot([1.0, 4.5], [5.0, 5.0], color='#1565c0', lw=1.0, linestyle='--')
    ax.fill_between([1.0, 4.5], 1.5, 5.0, color='#1565c0', alpha=0.06)
    ax.text(2.75, 2.5, r'$\mathbf{0.010\ \mathrm{mol\ dm^{-3}}\ \mathrm{Cu^{2+}(aq)}}$' '\n(Dilute: Oxidation occurs)', fontsize=6.5, color='#0b1b36', ha='center', fontweight='bold')

    # Cu electrode left (Anode)
    ax.fill_between([2.2, 2.6], 3.0, 7.5, color='#bcaaa4')
    ax.plot([2.2, 2.6, 2.6, 2.2, 2.2], [3.0, 3.0, 7.5, 7.5, 3.0], color='#5d4037', lw=1.0)
    ax.text(2.4, 8.0, r'$\mathbf{Cu(s)\ Anode}$' '\n' r'$(E < E^\circ)$', fontsize=6.8, color='#0b1b36', ha='center', fontweight='bold')

    # Right beaker: Concentrated Cu2+ (1.00 mol dm-3)
    ax.plot([7.5, 7.5, 11.0, 11.0], [6.5, 1.5, 1.5, 6.5], color='#0b1b36', lw=1.8)
    ax.plot([7.5, 11.0], [5.0, 5.0], color='#1565c0', lw=1.0, linestyle='--')
    ax.fill_between([7.5, 11.0], 1.5, 5.0, color='#1565c0', alpha=0.25)
    ax.text(9.25, 2.5, r'$\mathbf{1.00\ \mathrm{mol\ dm^{-3}}\ \mathrm{Cu^{2+}(aq)}}$' '\n(Concentrated: Reduction occurs)', fontsize=6.5, color='#1565c0', ha='center', fontweight='bold')

    # Cu electrode right (Cathode)
    ax.fill_between([9.4, 9.8], 3.0, 7.5, color='#bcaaa4')
    ax.plot([9.4, 9.8, 9.8, 9.4, 9.4], [3.0, 3.0, 7.5, 7.5, 3.0], color='#5d4037', lw=1.0)
    ax.text(9.6, 8.0, r'$\mathbf{Cu(s)\ Cathode}$' '\n' r'$(E = E^\circ)$', fontsize=6.8, color='#a81717', ha='center', fontweight='bold')

    # Salt bridge
    ax.plot([3.5, 3.5, 4.0, 4.0], [3.5, 6.8, 6.8, 3.5], color='#2e7d32', lw=1.2)
    ax.plot([8.0, 8.0, 8.5, 8.5], [3.5, 6.8, 6.8, 3.5], color='#2e7d32', lw=1.2)
    ax.plot([3.5, 8.5], [6.8, 6.8], color='#2e7d32', lw=1.2)
    ax.plot([4.0, 8.0], [6.4, 6.4], color='#2e7d32', lw=1.2)
    ax.fill_between([3.5, 4.0], 3.5, 6.4, color='#a5d6a7', alpha=0.6)
    ax.fill_between([8.0, 8.5], 3.5, 6.4, color='#a5d6a7', alpha=0.6)
    ax.fill_between([4.0, 8.0], 6.4, 6.8, color='#a5d6a7', alpha=0.6)
    ax.text(6.0, 7.1, r'$\mathbf{Salt\ Bridge}\ (\mathrm{KNO_3})$', fontsize=6.5, color='#2e7d32', ha='center', fontweight='bold')

    # Voltmeter
    ax.plot([2.4, 2.4, 5.4], [7.5, 9.2, 9.2], color='#0b1b36', lw=1.4)
    ax.plot([6.6, 9.6, 9.6], [9.2, 9.2, 7.5], color='#0b1b36', lw=1.4)
    circle = plt.Circle((6.0, 9.2), 0.6, color='#0b1b36', fill=True, facecolor='#ffffff', lw=1.5)
    ax.add_patch(circle)
    ax.text(6.0, 9.05, r'$\mathbf{V}$', fontsize=9.0, color='#0b1b36', ha='center', va='center', fontweight='bold')
    ax.text(6.0, 9.9, r'$E_\mathrm{cell} = \frac{0.059}{2}\log\left(\frac{1.00}{0.010}\right) = +0.059\ \mathrm{V}$', fontsize=7.2, color='#a81717', ha='center', fontweight='bold')

    # Nernst formula box
    ax.text(6.0, 0.4, r'$\mathbf{Nernst\ Equation:\ } E = E^\circ + \frac{0.059}{z}\log[\mathrm{Cu^{2+}}]\quad \Rightarrow\quad E_\mathrm{cell} = \frac{0.059}{z}\log\left(\frac{[\mathrm{Cu^{2+}}]_\mathrm{conc}}{[\mathrm{Cu^{2+}}]_\mathrm{dil}}\right)$',
            fontsize=6.8, color='#0b1b36', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fa', edgecolor='#dcd8d0', lw=0.8))

    out_file = os.path.join(fig_dir, "a2_t24_concentration_cell.png")
    fig.savefig(out_file, dpi=220, bbox_inches='tight')
    plt.close(fig)
    print(f"Created: {out_file}")

if __name__ == "__main__":
    create_she_apparatus()
    create_electrochemical_cell()
    create_electrolysis_coulometer()
    create_alkaline_fuel_cell()
    create_concentration_cell()
    print("All Topic 24 figures successfully generated.")
