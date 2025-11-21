#!/usr/bin/env python3
"""
Figure 1: Natural Experiment Timeline (1960-2024)
Somalia Federal vs Somalilandia Constitutional Divergence

Author: Adrian Lerer
Date: November 21, 2025
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np

# Set publication-quality parameters
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.linewidth'] = 1.5

# Create figure and axis
fig, ax = plt.subplots()

# Define timeline parameters
years = np.arange(1960, 2025, 5)
somalia_y = 0.7  # Somalia Federal track
somalilandia_y = 0.3  # Somalilandia track

# Background shading: Common baseline (1960-1991)
ax.axvspan(1960, 1991, alpha=0.15, color='gray', label='Common Baseline (1960-1991)')

# Main timeline
ax.plot([1960, 2024], [somalia_y, somalia_y], 'o-', color='#d62728', linewidth=3, 
        markersize=0, label='Somalia Federal (CLI 0.76)', alpha=0.7)
ax.plot([1960, 2024], [somalilandia_y, somalilandia_y], 'o-', color='#1f77b4', linewidth=3,
        markersize=0, label='Somalilandia (CLI 0.54)', alpha=0.7)

# Exogenous shock: 1991 state collapse
ax.axvline(x=1991, color='red', linewidth=3, linestyle='--', alpha=0.6, label='1991 State Collapse')
ax.text(1991, 0.95, 'EXOGENOUS SHOCK\nState Collapse', ha='center', va='top', 
        fontsize=10, fontweight='bold', color='red',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='red', alpha=0.8))

# ===== COMMON BASELINE EVENTS (1960-1991) =====
common_events = [
    (1960, 0.5, '1960: Independence & Union\n(British Somalilandia + Italian Somalia)', 'black'),
    (1969, 0.5, '1969: Siad Barre\nAuthoritarian Regime Begins', 'black'),
]

for year, y_pos, text, color in common_events:
    ax.plot(year, y_pos, 'o', markersize=10, color=color, zorder=5)
    ax.text(year, y_pos - 0.08, text, ha='center', va='top', fontsize=9, 
            bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='black', alpha=0.7))

# ===== SOMALIA FEDERAL EVENTS (1991-2024) =====
somalia_events = [
    (2000, somalia_y, 'Arta Conference\n4.5 Clan Formula', '#d62728', 'top'),
    (2012, somalia_y, 'Provisional Constitution\n(Aug 1) → Still Provisional 2024', '#d62728', 'bottom'),
    (2021, somalia_y, 'Farmajo Crisis\nTerm Extension Revoked', '#d62728', 'top'),
    (2024, somalia_y, '2024: Freedom House 8/100\nNo Direct Elections (56 years)', '#d62728', 'bottom'),
]

for year, y_pos, text, color, valign in somalia_events:
    ax.plot(year, y_pos, 's', markersize=12, color=color, zorder=5, markeredgecolor='darkred', markeredgewidth=1.5)
    if valign == 'top':
        ax.text(year, y_pos + 0.05, text, ha='center', va='bottom', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffcccc', edgecolor='darkred', alpha=0.9))
    else:
        ax.text(year, y_pos - 0.05, text, ha='center', va='top', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffcccc', edgecolor='darkred', alpha=0.9))

# ===== SOMALILANDIA EVENTS (1991-2024) =====
somalilandia_events = [
    (1991, somalilandia_y, 'Independence\nDeclaration (May 18)', '#1f77b4', 'bottom'),
    (1993, somalilandia_y, 'Borama Conference\n4 months consultation', '#1f77b4', 'top'),
    (2001, somalilandia_y, 'Constitutional Referendum\n97.1% YES, 99.9% turnout', '#1f77b4', 'bottom'),
    (2010, somalilandia_y, 'Opposition Victory\nSilanyo defeats Riyale', '#1f77b4', 'top'),
    (2021, somalilandia_y, 'Parliamentary Elections\nOpposition Coalition Victory', '#1f77b4', 'bottom'),
    (2024, somalilandia_y, '2024: Freedom House 43.7/100\nIrro Victory (Nov 13)', '#1f77b4', 'top'),
]

for year, y_pos, text, color, valign in somalilandia_events:
    ax.plot(year, y_pos, '^', markersize=12, color=color, zorder=5, markeredgecolor='darkblue', markeredgewidth=1.5)
    if valign == 'top':
        ax.text(year, y_pos + 0.05, text, ha='center', va='bottom', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#cce5ff', edgecolor='darkblue', alpha=0.9))
    else:
        ax.text(year, y_pos - 0.05, text, ha='center', va='top', fontsize=8,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#cce5ff', edgecolor='darkblue', alpha=0.9))

# ===== KEY ANNOTATIONS =====
annotations = [
    (1991, 0.12, 'CRITICAL JUNCTURE: Exogenous shock creates natural experiment', 'red', 'italic'),
    (2001, 0.12, 'Somalilandia: Bottom-up legitimacy (97.1% referendum)', '#1f77b4', 'normal'),
    (2012, 0.88, 'Somalia: Top-down rigidity (provisional constitution 13 years)', '#d62728', 'normal'),
    (2024, 0.12, 'Outcomes Divergence: FH 43.7 vs 8 (6x), Deaths 40 vs 3,116/year (78x)', 'black', 'bold'),
]

for year, y_pos, text, color, style in annotations:
    ax.text(year, y_pos, text, ha='center', va='center', fontsize=9, 
            color=color, fontstyle=style if style != 'bold' else 'normal',
            fontweight='bold' if style == 'bold' else 'normal',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=color, alpha=0.9, linewidth=2))

# Formatting
ax.set_xlim(1958, 2026)
ax.set_ylim(0.05, 1.0)
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('')
ax.set_yticks([somalilandia_y, somalia_y])
ax.set_yticklabels(['Somalilandia\n(CLI 0.54 - Flexible)', 'Somalia Federal\n(CLI 0.76 - Rigid)'], fontsize=11, fontweight='bold')
ax.set_xticks(years)
ax.grid(True, alpha=0.3, linestyle='--', axis='x')

# Title
ax.set_title('Figure 1. Natural Experiment Timeline: Somalia Federal vs Somalilandia Constitutional Divergence (1960-2024)',
             fontsize=14, fontweight='bold', pad=20)

# Legend
legend_elements = [
    mpatches.Patch(facecolor='gray', alpha=0.15, label='Common Baseline (1960-1991)'),
    plt.Line2D([0], [0], color='red', linewidth=3, linestyle='--', label='1991 State Collapse (Exogenous Shock)'),
    plt.Line2D([0], [0], color='#d62728', linewidth=3, marker='s', markersize=8, label='Somalia Federal (CLI 0.76 - High Rigidity)'),
    plt.Line2D([0], [0], color='#1f77b4', linewidth=3, marker='^', markersize=8, label='Somalilandia (CLI 0.54 - Low Rigidity)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10, framealpha=0.95, edgecolor='black')

# Tight layout
plt.tight_layout()

# Save figure
output_dir = '/home/user/webapp/papers/drafts/somalia_somalilandia_ept/figures'
import os
os.makedirs(output_dir, exist_ok=True)

# Save as high-resolution PDF (vector format)
plt.savefig(f'{output_dir}/figure1_timeline.pdf', dpi=300, bbox_inches='tight')
print(f"✅ Saved: {output_dir}/figure1_timeline.pdf (vector PDF)")

# Save as high-resolution PNG (raster format)
plt.savefig(f'{output_dir}/figure1_timeline.png', dpi=300, bbox_inches='tight')
print(f"✅ Saved: {output_dir}/figure1_timeline.png (300 DPI)")

# Show plot
plt.show()

print("\n" + "="*80)
print("FIGURE 1 CAPTION:")
print("="*80)
print("""
Figure 1. Natural Experiment Timeline: Somalia Federal vs Somalilandia Constitutional 
Divergence (1960-2024)

The 1991 state collapse created an exogenous shock enabling divergent constitutional paths 
despite common baseline (1960-1991 Barre regime). Somalia Federal adopted rigid top-down 
institutions (CLI 0.76): 4.5 clan formula (2000-present, 0 amendments), provisional 
constitution (2012-present, 13 years without finalization), no direct elections (1969-2024). 
Somalilandia pursued flexible bottom-up constitutionalism (CLI 0.54): Borama/Hargeisa 
conferences (1993-1997), referendum legitimacy (2001, 97.1% approval, 99.9% turnout), 
direct elections (2003-2024), peaceful opposition victories (2010, 2021, 2024). By 2024, 
outcomes diverged: Somalilandia Freedom House score 6x higher (43.7 vs 8), conflict deaths 
78x lower (~40 vs ~3,116 annually), demonstrating CLI correlation with governance quality.

Sources: Lewis (2002); Bradbury (2008); Federal Republic of Somalia (2012); Republic of 
Somalilandia (2001); Freedom House (2024); UCDP/ACLED (2015-2024); author compilation.
""")
print("="*80)
