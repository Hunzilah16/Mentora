"""
Generate high-resolution figures for Topic 6: Electrochemistry.
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
# Figure 1: Electrolysis of Concentrated Aqueous NaCl (Brine)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.4), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Beaker
beaker = plt.Rectangle((1.5, 1.0), 7.0, 5.0, facecolor='#e1f5fe', edgecolor='#0b1b36', lw=2.0)
ax.add_patch(beaker)

# Electrolyte level
ax.plot([1.5, 8.5], [5.2, 5.2], color='#0288d1', lw=1.5, linestyle=':')
ax.text(5.0, 1.4, r'Concentrated Aqueous $\mathrm{NaCl}$ (Brine): $\mathrm{Na^+,\ Cl^-,\ H^+,\ OH^-}$',
        ha='center', fontsize=8, fontweight='bold', color='#01579b')

# Anode (+) Carbon/Titanium
anode = plt.Rectangle((2.8, 2.2), 0.8, 4.0, facecolor='#424242', edgecolor='#212121', lw=1.5)
ax.add_patch(anode)
ax.text(3.2, 6.4, 'ANODE (+)\nCarbon', ha='center', fontsize=7.5, fontweight='bold', color='#a81717')
ax.annotate(r'$2\mathrm{Cl^-} \rightarrow \mathrm{Cl_2} + 2\mathrm{e^-}$' '\n(Oxidation)',
            xy=(2.8, 3.8), xytext=(0.5, 4.5),
            arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.2),
            fontsize=7.5, color='#a81717', fontweight='bold')

# Bubbles at Anode (Cl2)
for by in [2.8, 3.5, 4.2, 4.8]:
    ax.scatter([3.0, 3.4], [by, by+0.2], s=25, color='#cddc39', edgecolors='#827717')
ax.text(2.3, 2.5, r'$\mathrm{Cl_2(g)}$', fontsize=8, fontweight='bold', color='#827717')

# Cathode (-) Carbon/Steel
cathode = plt.Rectangle((6.4, 2.2), 0.8, 4.0, facecolor='#78909c', edgecolor='#37474f', lw=1.5)
ax.add_patch(cathode)
ax.text(6.8, 6.4, 'CATHODE (-)\nSteel/Carbon', ha='center', fontsize=7.5, fontweight='bold', color='#1565c0')
ax.annotate(r'$2\mathrm{H^+} + 2\mathrm{e^-} \rightarrow \mathrm{H_2}$' '\n(Reduction)',
            xy=(7.2, 3.8), xytext=(7.8, 4.5),
            arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.2),
            fontsize=7.5, color='#1565c0', fontweight='bold')

# Bubbles at Cathode (H2)
for by in [2.7, 3.3, 4.0, 4.7]:
    ax.scatter([6.6, 7.0], [by, by+0.2], s=25, color='#ffffff', edgecolors='#1565c0')
ax.text(7.3, 2.5, r'$\mathrm{H_2(g)}$', fontsize=8, fontweight='bold', color='#1565c0')

# External Circuit & DC Power Supply
ax.plot([3.2, 3.2, 4.5], [6.2, 6.8, 6.8], color='#212121', lw=1.8)
ax.plot([6.8, 6.8, 5.5], [6.2, 6.8, 6.8], color='#212121', lw=1.8)
# Battery symbol
ax.plot([4.5, 4.5], [6.5, 7.1], color='#a81717', lw=2.5) # long +
ax.plot([4.8, 4.8], [6.6, 7.0], color='#212121', lw=1.5) # short -
ax.plot([5.1, 5.1], [6.5, 7.1], color='#a81717', lw=2.5) # long +
ax.plot([5.5, 5.5], [6.6, 7.0], color='#212121', lw=1.5) # short -
ax.text(4.4, 7.2, '+', color='#a81717', fontweight='bold', fontsize=10)
ax.text(5.6, 7.2, '-', color='#1565c0', fontweight='bold', fontsize=10)
ax.text(5.0, 5.9, 'DC Power', ha='center', fontsize=7.5, fontweight='bold', color='#212121')

ax.set_title(r'Electrolysis of Concentrated Aqueous Sodium Chloride (Brine)', fontsize=10, fontweight='bold', color='#0b1b36', pad=12)
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'electrolysis_aqueous_nacl.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 2: Industrial Refining of Copper
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.4), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Tank
tank = plt.Rectangle((1.5, 1.0), 7.0, 5.0, facecolor='#e0f2f1', edgecolor='#004d40', lw=2.0)
ax.add_patch(tank)

# Electrolyte
ax.plot([1.5, 8.5], [5.2, 5.2], color='#00897b', lw=1.5, linestyle=':')
ax.text(5.0, 1.5, r'Electrolyte: Aqueous $\mathrm{CuSO_4} + \mathrm{H_2SO_4}$',
        ha='center', fontsize=8, fontweight='bold', color='#004d40')

# Impure Anode (thick block)
anode_cu = plt.Rectangle((2.6, 2.0), 1.2, 4.2, facecolor='#bcaaa4', edgecolor='#5d4037', lw=1.8)
ax.add_patch(anode_cu)
ax.text(3.2, 6.4, 'ANODE (+)\nImpure Blister Cu', ha='center', fontsize=7.5, fontweight='bold', color='#a81717')
ax.annotate(r'$\mathrm{Cu(s)} \rightarrow \mathrm{Cu^{2+}(aq)} + 2\mathrm{e^-}$' '\n(Anode dissolves)',
            xy=(2.6, 3.5), xytext=(0.4, 4.0),
            arrowprops=dict(arrowstyle='->', color='#a81717', lw=1.2),
            fontsize=7.5, color='#a81717', fontweight='bold')

# Anode slime at bottom
slime = plt.Polygon([[2.5, 1.0], [3.9, 1.0], [3.6, 1.4], [2.8, 1.4]], facecolor='#795548', edgecolor='#3e2723')
ax.add_patch(slime)
ax.annotate('Anode sludge / slime\n(Precious Ag, Au, Pt)', xy=(3.2, 1.2), xytext=(1.2, 2.2),
            arrowprops=dict(arrowstyle='->', color='#5d4037', lw=1.0),
            fontsize=7.5, color='#3e2723', fontweight='semibold')

# Pure Cathode (thin sheet that grows)
cathode_cu = plt.Rectangle((6.8, 2.0), 0.4, 4.2, facecolor='#ff8a65', edgecolor='#d84315', lw=1.8)
ax.add_patch(cathode_cu)
ax.text(7.0, 6.4, 'CATHODE (-)\nPure Copper Sheet', ha='center', fontsize=7.5, fontweight='bold', color='#1565c0')
ax.annotate(r'$\mathrm{Cu^{2+}(aq)} + 2\mathrm{e^-} \rightarrow \mathrm{Cu(s)}$' '\n(Pure Cu deposits)',
            xy=(7.2, 3.5), xytext=(7.6, 4.0),
            arrowprops=dict(arrowstyle='->', color='#1565c0', lw=1.2),
            fontsize=7.5, color='#1565c0', fontweight='bold')

# Cu2+ migration arrow
ax.annotate(r'$\mathrm{Cu^{2+}}$ migration', xy=(6.6, 3.2), xytext=(4.0, 3.2),
            arrowprops=dict(arrowstyle='->', color='#00897b', lw=2.0),
            fontsize=8, fontweight='bold', color='#004d40')

# External circuit
ax.plot([3.2, 3.2, 4.5], [6.2, 6.8, 6.8], color='#212121', lw=1.8)
ax.plot([7.0, 7.0, 5.5], [6.2, 6.8, 6.8], color='#212121', lw=1.8)
ax.plot([4.5, 4.5], [6.5, 7.1], color='#a81717', lw=2.5)
ax.plot([5.5, 5.5], [6.6, 7.0], color='#212121', lw=1.5)
ax.text(5.0, 6.2, 'DC Supply', ha='center', fontsize=7.5, fontweight='bold', color='#212121')

ax.set_title('Industrial Electrolytic Purification (Refining) of Copper', fontsize=10, fontweight='bold', color='#0b1b36', pad=12)
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'copper_refining_cell.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 3: Redox Titration Setup (KMnO4 with Fe2+)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.0, 3.4), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Burette
burette = plt.Rectangle((4.6, 2.5), 0.8, 5.0, facecolor='#ede7f6', edgecolor='#4a148c', lw=1.5)
ax.add_patch(burette)
# Purple liquid inside burette
kmno4_liq = plt.Rectangle((4.65, 2.8), 0.7, 4.4, facecolor='#7b1fa2', edgecolor='none')
ax.add_patch(kmno4_liq)
ax.text(4.2, 5.0, r'Burette:' '\n' r'Standard $\mathrm{KMnO_4(aq)}$' '\n(Deep Purple)',
        ha='right', fontsize=7.5, fontweight='bold', color='#4a148c')

# Tap / Stopcock
ax.plot([4.4, 5.6], [2.5, 2.5], color='#212121', lw=2.0)
ax.plot([5.0, 5.0], [2.2, 2.5], color='#212121', lw=2.0)

# Conical Flask
flask = plt.Polygon([[3.0, 0.4], [7.0, 0.4], [5.6, 1.8], [4.4, 1.8]], facecolor='#fce4ec', edgecolor='#880e4f', lw=1.8)
ax.add_patch(flask)
ax.text(5.0, 0.8, r'$\mathrm{Fe^{2+}(aq)} + \mathrm{H_2SO_4(aq)}$', ha='center', fontsize=8, fontweight='bold', color='#880e4f')

# End-point annotation
ax.annotate('Self-indicating End-Point:\nFirst permanent pale pink\n' r'($\mathrm{MnO_4^-}$ in slight excess)',
            xy=(6.5, 1.0), xytext=(7.2, 2.5),
            arrowprops=dict(arrowstyle='->', color='#ad1457', lw=1.3),
            fontsize=7.5, color='#ad1457', fontweight='bold')

# Half-equation box
ax.text(1.8, 1.2, r'$\mathrm{MnO_4^-} + 8\mathrm{H^+} + 5\mathrm{e^-} \rightarrow \mathrm{Mn^{2+}} + 4\mathrm{H_2O}$' '\n'
        r'$\mathrm{Fe^{2+}} \rightarrow \mathrm{Fe^{3+}} + \mathrm{e^-}$',
        fontsize=7, color='#0b1b36', bbox=dict(boxstyle='round,pad=0.3', facecolor='#f5f5f5', edgecolor='#9e9e9e'))

ax.set_title(r'Redox Titration: Standard $\mathrm{KMnO_4}$ Against Acidified $\mathrm{Fe^{2+}}$', fontsize=9.5, fontweight='bold', color='#0b1b36')
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'redox_titration_permanganate.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 4: Disproportionation of Chlorine
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=200)
ax.set_xlim(-1, 9)
ax.set_ylim(-2, 7)

# Horizontal line at 0 (Cl2)
ax.axhline(0, color='#666666', linestyle='--', lw=1.0)

# Points for oxidation numbers
# Cold dilute NaOH: Cl2 (0) -> Cl- (-1) and ClO- (+1)
ax.scatter([2, 2, 2], [0, -1, 1], color=['#2e7d32', '#1565c0', '#c62828'], s=120, zorder=5)
ax.plot([2, 2], [0, -1], '->', color='#1565c0', lw=2.0)
ax.plot([2, 2], [0, 1], '->', color='#c62828', lw=2.0)
ax.text(2, -0.2, r'$\mathrm{Cl_2\ (0)}$', ha='right', fontsize=8.5, fontweight='bold', color='#2e7d32')
ax.text(2.3, -1.0, r'$\mathrm{Cl^-\ (-1)}$ (Reduced)', va='center', fontsize=8, color='#1565c0', fontweight='bold')
ax.text(2.3, 1.0, r'$\mathrm{ClO^-\ (+1)}$ (Oxidised)', va='center', fontsize=8, color='#c62828', fontweight='bold')
ax.text(2, -1.8, 'Cold Dilute NaOH (15 °C)\n' r'$\mathrm{Cl_2 + 2OH^- \rightarrow Cl^- + ClO^- + H_2O}$',
        ha='center', fontsize=7.5, fontweight='semibold', color='#0b1b36')

# Hot conc NaOH: Cl2 (0) -> Cl- (-1) and ClO3- (+5)
ax.scatter([6.5, 6.5, 6.5], [0, -1, 5], color=['#2e7d32', '#1565c0', '#e65100'], s=120, zorder=5)
ax.plot([6.5, 6.5], [0, -1], '->', color='#1565c0', lw=2.0)
ax.plot([6.5, 6.5], [0, 5], '->', color='#e65100', lw=2.0)
ax.text(6.5, -0.2, r'$\mathrm{Cl_2\ (0)}$', ha='right', fontsize=8.5, fontweight='bold', color='#2e7d32')
ax.text(6.8, -1.0, r'$\mathrm{Cl^-\ (-1)}$ (Reduced)', va='center', fontsize=8, color='#1565c0', fontweight='bold')
ax.text(6.8, 5.0, r'$\mathrm{ClO_3^-\ (+5)}$ (Oxidised)', va='center', fontsize=8, color='#e65100', fontweight='bold')
ax.text(6.5, -1.8, 'Hot Concentrated NaOH (70 °C)\n' r'$\mathrm{3Cl_2 + 6OH^- \rightarrow 5Cl^- + ClO_3^- + 3H_2O}$',
        ha='center', fontsize=7.5, fontweight='semibold', color='#0b1b36')

ax.set_ylabel('Oxidation State of Chlorine', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_yticks([-1, 0, 1, 2, 3, 4, 5])
ax.set_xticks([])
ax.set_title('Disproportionation of Chlorine in Cold vs Hot Aqueous Alkali', fontsize=10, fontweight='bold', color='#0b1b36', pad=10)
ax.grid(True, axis='y', linestyle=':', alpha=0.6)

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'disproportionation_concept.png'), dpi=200)
plt.close(fig)

print("Generated Topic 6 figures successfully!")
