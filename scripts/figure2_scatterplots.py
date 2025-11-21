#!/usr/bin/env python3
"""
Figure 2: CLI vs Governance Outcomes Scatterplots
Panel A: CLI vs Democracy (Freedom House)
Panel B: CLI vs Violence (Log Annual Deaths)

Author: Adrian Lerer
Date: November 21, 2025
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Set publication-quality parameters
plt.rcParams['figure.figsize'] = (14, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.linewidth'] = 1.5

# Data
entities = ['Somalia Federal', 'Somalilandia']
cli_scores = np.array([0.76, 0.54])
fh_scores = np.array([8, 43.7])
annual_deaths = np.array([3116, 40])
log_deaths = np.log10(annual_deaths)

# Colors
somalia_color = '#d62728'
somalilandia_color = '#1f77b4'
colors = [somalia_color, somalilandia_color]

# Create figure with two panels
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ===== PANEL A: CLI vs Freedom House Score =====
ax1.scatter(cli_scores, fh_scores, s=200, c=colors, alpha=0.7, edgecolors='black', linewidths=2, zorder=3)

# Add labels for points
for i, entity in enumerate(entities):
    offset = 3 if i == 0 else -3
    ax1.annotate(entity, (cli_scores[i], fh_scores[i]), 
                textcoords="offset points", xytext=(0, offset), ha='center',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='black', alpha=0.85))

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(cli_scores, fh_scores)
x_line = np.linspace(0.5, 0.8, 100)
y_line = slope * x_line + intercept
ax1.plot(x_line, y_line, '--', color='gray', linewidth=2, alpha=0.7, label=f'Linear fit (r = {r_value:.2f})')

# Formatting Panel A
ax1.set_xlabel('Constitutional Lock-In Index (CLI)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Freedom House Score (0-100)', fontsize=12, fontweight='bold')
ax1.set_title('Panel A: CLI vs Democracy\n(Lower CLI → Higher Freedom House Score)', 
             fontsize=13, fontweight='bold', pad=15)
ax1.set_xlim(0.50, 0.80)
ax1.set_ylim(-5, 50)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(loc='upper right', fontsize=10, framealpha=0.95)

# Add correlation annotation
ax1.text(0.65, 35, f'r = {r_value:.2f}\nN = 2', 
        ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', edgecolor='black', alpha=0.8))

# Add interpretation box
ax1.text(0.65, 15, 'Higher CLI (rigidity)\n→ Lower democracy', 
        ha='center', va='center', fontsize=9, style='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffcccc', edgecolor='red', alpha=0.7))

# ===== PANEL B: CLI vs Log(Annual Deaths) =====
ax2.scatter(cli_scores, log_deaths, s=200, c=colors, alpha=0.7, edgecolors='black', linewidths=2, zorder=3)

# Add labels for points
for i, entity in enumerate(entities):
    offset = 0.15 if i == 0 else -0.15
    ax2.annotate(entity, (cli_scores[i], log_deaths[i]), 
                textcoords="offset points", xytext=(0, offset * 50), ha='center',
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='black', alpha=0.85))

# Linear regression
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(cli_scores, log_deaths)
y_line2 = slope2 * x_line + intercept2
ax2.plot(x_line, y_line2, '--', color='gray', linewidth=2, alpha=0.7, label=f'Linear fit (r = {r_value2:.2f})')

# Formatting Panel B
ax2.set_xlabel('Constitutional Lock-In Index (CLI)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Log₁₀(Annual Conflict Deaths)', fontsize=12, fontweight='bold')
ax2.set_title('Panel B: CLI vs Violence\n(Lower CLI → Lower Conflict Deaths)', 
             fontsize=13, fontweight='bold', pad=15)
ax2.set_xlim(0.50, 0.80)
ax2.set_ylim(1.4, 3.6)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(loc='upper left', fontsize=10, framealpha=0.95)

# Add correlation annotation
ax2.text(0.65, 3.2, f'r = {r_value2:.2f}\nN = 2', 
        ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', edgecolor='black', alpha=0.8))

# Add interpretation box
ax2.text(0.65, 2.0, 'Higher CLI (rigidity)\n→ Higher violence', 
        ha='center', va='center', fontsize=9, style='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffcccc', edgecolor='red', alpha=0.7))

# Add death count annotations
ax2.text(0.76, 3.55, '3,116 deaths/year', ha='center', fontsize=8, color=somalia_color, fontweight='bold')
ax2.text(0.54, 1.5, '40 deaths/year', ha='center', fontsize=8, color=somalilandia_color, fontweight='bold')

# Super title
fig.suptitle('Figure 2. Constitutional Lock-In Index (CLI) Correlates with Governance Outcomes',
            fontsize=15, fontweight='bold', y=1.00)

# Tight layout
plt.tight_layout(rect=[0, 0, 1, 0.97])

# Save figure
output_dir = '/home/user/webapp/papers/drafts/somalia_somalilandia_ept/figures'
import os
os.makedirs(output_dir, exist_ok=True)

# Save as high-resolution PDF (vector format)
plt.savefig(f'{output_dir}/figure2_scatterplots.pdf', dpi=300, bbox_inches='tight')
print(f"✅ Saved: {output_dir}/figure2_scatterplots.pdf (vector PDF)")

# Save as high-resolution PNG (raster format)
plt.savefig(f'{output_dir}/figure2_scatterplots.png', dpi=300, bbox_inches='tight')
print(f"✅ Saved: {output_dir}/figure2_scatterplots.png (300 DPI)")

# Show plot
plt.show()

print("\n" + "="*80)
print("FIGURE 2 CAPTION:")
print("="*80)
print("""
Figure 2. Constitutional Lock-In Index (CLI) Correlates with Governance Outcomes

Panel A: Lower CLI predicts higher Freedom House democracy scores (r = -1.00, N=2). 
Somalilandia's flexible institutions (CLI 0.54) achieve 6x higher score (43.7) than 
Somalia Federal's rigid system (CLI 0.76, score 8). Panel B: Lower CLI predicts lower 
conflict intensity (r = +1.00, N=2). Somalilandia experiences 78x fewer annual deaths 
(~40) than Somalia Federal (~3,116), measured 2015-2024.

Methodological Note: Perfect correlations (r = ±1.00) are artifacts of N=2 natural 
experiment design, not universal laws. Correlations demonstrate CLI predictions hold in 
this paired comparison but require replication across additional cases (e.g., Latin 
America CLI studies) to establish generalizability. Log transformation applied to 
conflict deaths to normalize skewed distribution.

Sources: Author CLI calculations; Freedom House (2024); UCDP/ACLED (2015-2024).
""")
print("="*80)

print("\n" + "="*80)
print("DATA VALUES:")
print("="*80)
print(f"Somalia Federal: CLI {cli_scores[0]}, FH {fh_scores[0]}, Deaths {annual_deaths[0]}, Log {log_deaths[0]:.2f}")
print(f"Somalilandia: CLI {cli_scores[1]}, FH {fh_scores[1]}, Deaths {annual_deaths[1]}, Log {log_deaths[1]:.2f}")
print(f"Panel A correlation: r = {r_value:.2f} (perfect negative)")
print(f"Panel B correlation: r = {r_value2:.2f} (perfect positive)")
print("="*80)
