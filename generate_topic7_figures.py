"""
Generate high-resolution figures for Topic 7: Equilibria.
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
# Figure 1: Haber Process Equilibrium Yield vs Temperature
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.4), dpi=200)

temp = np.linspace(200, 700, 200)

# Curves for 400 atm, 200 atm, 50 atm
yield_400 = 100 / (1 + np.exp(0.015 * (temp - 380)))
yield_200 = 100 / (1 + np.exp(0.015 * (temp - 320)))
yield_50  = 100 / (1 + np.exp(0.015 * (temp - 260)))

ax.plot(temp, yield_400, color='#1565c0', lw=2.0, label='400 atm')
ax.plot(temp, yield_200, color='#2e7d32', lw=2.2, label='200 atm (Compromise Pressure)')
ax.plot(temp, yield_50,  color='#a81717', lw=2.0, label='50 atm')

# Compromise operating point at 450 °C and 200 atm
ax.axvline(450, color='#c62828', linestyle=':', lw=1.5)
ax.plot(450, 100 / (1 + np.exp(0.015 * (450 - 320))), 'o', color='#c62828', markersize=7)
ax.annotate('Compromise Conditions:\n450 °C, 200 atm, Fe catalyst\n(~15% yield per pass)',
            xy=(450, 15), xytext=(480, 45),
            arrowprops=dict(arrowstyle='->', color='#c62828', lw=1.3),
            fontsize=8, color='#c62828', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff3e0', edgecolor='#c62828'))

ax.set_title(r'Haber Process: Equilibrium % Yield of $\mathrm{NH_3}$ vs Temperature', fontsize=10, fontweight='bold', color='#0b1b36', pad=10)
ax.set_xlabel(r'Temperature / $^\circ\mathrm{C}$', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_ylabel(r'Equilibrium Yield of $\mathrm{NH_3}$ / %', fontsize=9, fontweight='bold', color='#0b1b36')
ax.set_xlim(200, 700)
ax.set_ylim(0, 100)
ax.grid(True, linestyle=':', alpha=0.6, color='#99aab5')
ax.legend(frameon=True, facecolor='#f8f9fa', fontsize=8, loc='upper right')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'haber_process_compromise.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 2: Establishment of Dynamic Equilibrium (Rates & Concs)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.0), dpi=200)

t = np.linspace(0, 10, 200)

# Rates
r_forward = 1.0 + 3.0 * np.exp(-0.8 * t)
r_reverse = 1.0 - 1.0 * np.exp(-0.8 * t)

ax1.plot(t, r_forward, color='#1565c0', lw=2.0, label='Forward rate')
ax1.plot(t, r_reverse, color='#a81717', lw=2.0, label='Reverse rate')
ax1.axvline(5.0, color='#666666', linestyle='--', lw=1.2)
ax1.text(5.2, 3.2, 'Dynamic Equilibrium\n' r'($r_\mathrm{forward} = r_\mathrm{reverse}$)', fontsize=7.5, fontweight='bold', color='#0b1b36')
ax1.set_title('Reaction Rates vs Time', fontsize=9, fontweight='bold', color='#0b1b36')
ax1.set_xlabel('Time', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax1.set_ylabel('Reaction Rate', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax1.set_ylim(0, 4.5)
ax1.legend(frameon=True, facecolor='#f8f9fa', fontsize=7.5, loc='upper right')
ax1.grid(True, linestyle=':', alpha=0.6)

# Concentrations
c_reactants = 0.8 + 2.2 * np.exp(-0.8 * t)
c_products  = 1.5 * (1 - np.exp(-0.8 * t))

ax2.plot(t, c_reactants, color='#1565c0', lw=2.0, label='[Reactants]')
ax2.plot(t, c_products, color='#2e7d32', lw=2.0, label='[Products]')
ax2.axvline(5.0, color='#666666', linestyle='--', lw=1.2)
ax2.text(5.2, 2.3, 'Concentrations\nremain constant', fontsize=7.5, fontweight='bold', color='#0b1b36')
ax2.set_title('Concentrations vs Time', fontsize=9, fontweight='bold', color='#0b1b36')
ax2.set_xlabel('Time', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax2.set_ylabel('Concentration / mol dm⁻³', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax2.set_ylim(0, 3.5)
ax2.legend(frameon=True, facecolor='#f8f9fa', fontsize=7.5, loc='center right')
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'dynamic_equilibrium_rates.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 3: Le Chatelier Perturbation (Injecting Reactant)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=200)

# N2(g) + 3H2(g) <=> 2NH3(g)
# Region 1: 0 to 4 (Equilibrium)
t1 = np.linspace(0, 4, 50)
n2_1 = np.full_like(t1, 1.0)
h2_1 = np.full_like(t1, 2.5)
nh3_1 = np.full_like(t1, 1.8)

# At t = 4, extra N2 is injected: N2 jumps from 1.0 to 2.2
# Region 2: 4 to 10 (Re-establishing equilibrium)
t2 = np.linspace(4, 10, 100)
dt = t2 - 4
n2_2 = 1.6 + 0.6 * np.exp(-0.8 * dt)   # decreases from 2.2 towards 1.6
h2_2 = 2.5 - 0.7 * (1 - np.exp(-0.8 * dt)) # decreases from 2.5 to 1.8
nh3_2 = 1.8 + 0.5 * (1 - np.exp(-0.8 * dt)) # increases from 1.8 to 2.3

t_full = np.concatenate([t1, t2])
n2_full = np.concatenate([n2_1, n2_2])
h2_full = np.concatenate([h2_1, h2_2])
nh3_full = np.concatenate([nh3_1, nh3_2])

ax.plot(t_full, n2_full, color='#1565c0', lw=2.0, label=r'$[\mathrm{N_2}]$')
ax.plot(t_full, h2_full, color='#2e7d32', lw=2.0, label=r'$[\mathrm{H_2}]$')
ax.plot(t_full, nh3_full, color='#a81717', lw=2.0, label=r'$[\mathrm{NH_3}]$')

# Vertical line at perturbation
ax.axvline(4.0, color='#d32f2f', linestyle='--', lw=1.5)
ax.annotate(r'Extra $\mathrm{N_2}$ injected' '\nat t = 4 min', xy=(4.0, 2.2), xytext=(4.3, 2.7),
            arrowprops=dict(arrowstyle='->', color='#d32f2f', lw=1.2),
            fontsize=8, color='#d32f2f', fontweight='bold')

ax.annotate('Equilibrium shifts right\n' r'to consume added $\mathrm{N_2}$', xy=(7.0, 2.3), xytext=(6.5, 3.1),
            arrowprops=dict(arrowstyle='->', color='#0b1b36', lw=1.0),
            fontsize=7.5, color='#0b1b36', fontweight='semibold')

ax.set_title(r"Le Chatelier's Principle: Effect of Adding Reactant $\mathrm{N_2}$", fontsize=9.5, fontweight='bold', color='#0b1b36', pad=10)
ax.set_xlabel('Time / min', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax.set_ylabel(r'Concentration / $\mathrm{mol\ dm^{-3}}$', fontsize=8.5, fontweight='bold', color='#0b1b36')
ax.set_xlim(0, 10)
ax.set_ylim(0.5, 3.5)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(frameon=True, facecolor='#f8f9fa', fontsize=8, loc='lower left')

plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'le_chatelier_perturbation.png'), dpi=200)
plt.close(fig)

# -------------------------------------------------------------
# Figure 4: Brønsted-Lowry Conjugate Acid-Base Pairs
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 2.8), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Reaction: CH3COOH + H2O <=> CH3COO- + H3O+
# CH3COOH (Acid 1)
ax.text(1.5, 3.8, r'$\mathrm{CH_3COOH}$', ha='center', fontsize=11, fontweight='bold', color='#0b1b36')
ax.text(1.5, 3.0, 'Acid 1\n(Proton donor)', ha='center', fontsize=7.5, color='#0b1b36')

ax.text(2.8, 3.8, '+', ha='center', fontsize=12, fontweight='bold', color='#666666')

# H2O (Base 2)
ax.text(4.0, 3.8, r'$\mathrm{H_2O}$', ha='center', fontsize=11, fontweight='bold', color='#1565c0')
ax.text(4.0, 3.0, 'Base 2\n(Proton acceptor)', ha='center', fontsize=7.5, color='#1565c0')

# Equilibrium arrows
ax.text(5.2, 3.8, r'$\rightleftharpoons$', ha='center', fontsize=15, fontweight='bold', color='#212121')

# CH3COO- (Conjugate Base 1)
ax.text(6.4, 3.8, r'$\mathrm{CH_3COO^-}$', ha='center', fontsize=11, fontweight='bold', color='#0b1b36')
ax.text(6.4, 3.0, 'Conjugate Base 1\n(Proton acceptor)', ha='center', fontsize=7.5, color='#0b1b36')

ax.text(7.6, 3.8, '+', ha='center', fontsize=12, fontweight='bold', color='#666666')

# H3O+ (Conjugate Acid 2)
ax.text(8.8, 3.8, r'$\mathrm{H_3O^+}$', ha='center', fontsize=11, fontweight='bold', color='#1565c0')
ax.text(8.8, 3.0, 'Conjugate Acid 2\n(Proton donor)', ha='center', fontsize=7.5, color='#1565c0')

# Curved connection 1: Acid 1 to Conjugate Base 1 (top arc)
ax.annotate('', xy=(6.4, 4.6), xytext=(1.5, 4.6),
            arrowprops=dict(arrowstyle='<->', color='#a81717', lw=1.8, connectionstyle="arc3,rad=-0.3"))
ax.text(4.0, 5.5, r'Conjugate Acid-Base Pair 1 (differs by $\mathrm{H^+}$)', ha='center', fontsize=7.5, fontweight='bold', color='#a81717')

# Curved connection 2: Base 2 to Conjugate Acid 2 (bottom arc)
ax.annotate('', xy=(8.8, 2.2), xytext=(4.0, 2.2),
            arrowprops=dict(arrowstyle='<->', color='#2e7d32', lw=1.8, connectionstyle="arc3,rad=0.3"))
ax.text(6.4, 1.2, r'Conjugate Acid-Base Pair 2 (differs by $\mathrm{H^+}$)', ha='center', fontsize=7.5, fontweight='bold', color='#2e7d32')

ax.set_title(r'Brønsted-Lowry Theory: Proton Transfer & Conjugate Acid-Base Pairs', fontsize=9.5, fontweight='bold', color='#0b1b36')
plt.tight_layout()
fig.savefig(os.path.join(fig_dir, 'bronsted_lowry_conjugate_pairs.png'), dpi=200)
plt.close(fig)

print("Generated Topic 7 figures successfully!")
