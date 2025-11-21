#!/usr/bin/env python3
"""
Generate Figure 3: CLI × CLI_cultural Interaction Matrix
Shows four institutional configurations with collapse risk threshold
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import Rectangle, FancyBboxPatch

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(12, 10))

# Data points
entities = ['Somalia Federal', 'Somalilandia', 'Uruguay', 'Chile', 'Argentina']
cli = np.array([0.76, 0.54, 0.75, 0.68, 0.55])
cli_cultural = np.array([0.34, 0.70, 0.77, 0.65, 0.59])
colors = ['red', 'green', 'blue', 'orange', 'purple']
markers = ['X', 'o', 's', '^', 'D']
sizes = [300, 300, 200, 200, 200]

# Quadrant shading with transparency
ax.add_patch(Rectangle((0.60, 0.60), 0.40, 0.40, alpha=0.15, color='lightgreen', zorder=0))
ax.add_patch(Rectangle((0.60, 0.00), 0.40, 0.60, alpha=0.25, color='red', zorder=0))
ax.add_patch(Rectangle((0.00, 0.00), 0.60, 0.60, alpha=0.15, color='orange', zorder=0))
ax.add_patch(Rectangle((0.00, 0.60), 0.60, 0.40, alpha=0.15, color='lightblue', zorder=0))

# Collapse risk threshold curve (Interaction = 0.30)
x_threshold = np.linspace(0.30, 1.0, 1000)
y_threshold = 0.30 / x_threshold
ax.plot(x_threshold, y_threshold, 'k--', linewidth=3, label='Collapse Risk Threshold (0.30)', zorder=5)

# Fill danger zone (below threshold)
x_fill = np.linspace(0.30, 1.0, 1000)
y_fill = 0.30 / x_fill
ax.fill_between(x_fill, 0, y_fill, alpha=0.1, color='red', zorder=1)

# Plot data points
for i, entity in enumerate(entities):
    ax.scatter(cli[i], cli_cultural[i], s=sizes[i], c=colors[i], 
               marker=markers[i], edgecolors='black', linewidths=2,
               label=entity, zorder=10, alpha=0.9)
    
    # Add interaction score annotation
    interaction = cli[i] * cli_cultural[i]
    offset_x = 0.02 if entity != 'Somalia Federal' else -0.08
    offset_y = 0.03 if entity != 'Uruguay' else -0.04
    ax.annotate(f'{interaction:.2f}', 
                xy=(cli[i], cli_cultural[i]), 
                xytext=(cli[i] + offset_x, cli_cultural[i] + offset_y),
                fontsize=10, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='black'),
                zorder=11)

# Quadrant labels
ax.text(0.80, 0.80, 'Quadrant I\nSTABLE RIGIDITY\n(Uruguay)', 
        ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))

ax.text(0.80, 0.30, 'Quadrant II\nBRITTLE RIGIDITY ⚠️\n(Somalia Federal)\nDANGER ZONE', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='darkred',
        bbox=dict(boxstyle='round', facecolor='#ffcccc', alpha=0.8, edgecolor='red', linewidth=2))

ax.text(0.30, 0.30, 'Quadrant III\nCHAOTIC FRAGILITY\n(No cases)', 
        ha='center', va='center', fontsize=10, style='italic', color='gray',
        bbox=dict(boxstyle='round', facecolor='#ffe6cc', alpha=0.5))

ax.text(0.30, 0.80, 'Quadrant IV\nADAPTIVE STABILITY ✓\n(Somalilandia)\nOPTIMAL ZONE', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='darkgreen',
        bbox=dict(boxstyle='round', facecolor='#ccffcc', alpha=0.8, edgecolor='green', linewidth=2))

# Dividing lines
ax.axvline(x=0.60, color='gray', linestyle='-', linewidth=1.5, alpha=0.5, zorder=2)
ax.axhline(y=0.60, color='gray', linestyle='-', linewidth=1.5, alpha=0.5, zorder=2)

# Axes labels
ax.set_xlabel('CLI (Constitutional Lock-In Index)', fontsize=14, fontweight='bold')
ax.set_ylabel('CLI_cultural (Cultural Lock-In Index)', fontsize=14, fontweight='bold')
ax.set_title('Figure 3: CLI × CLI_cultural Interaction Matrix\nBrittle Rigidity vs Adaptive Stability', 
             fontsize=16, fontweight='bold', pad=20)

# Set limits
ax.set_xlim(0.25, 1.0)
ax.set_ylim(0.25, 1.0)

# Grid
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5, zorder=0)

# Legend
legend = ax.legend(loc='lower right', fontsize=10, framealpha=0.95, 
                   edgecolor='black', fancybox=True, shadow=True)
legend.set_zorder(20)

# Add text annotations
ax.text(0.97, 0.03, 'HIGH COLLAPSE RISK\n(Interaction < 0.30)', 
        ha='right', va='bottom', fontsize=9, style='italic', color='darkred',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#ffcccc', alpha=0.7))

ax.text(0.03, 0.97, 'LOW COLLAPSE RISK\n(Interaction > 0.30)', 
        ha='left', va='top', fontsize=9, style='italic', color='darkgreen',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='#ccffcc', alpha=0.7))

# Notes
notes = ('Notes: Interaction scores shown next to data points. Collapse risk threshold (CLI × CLI_cultural = 0.30) '
         'divides high-risk zone (below curve) from low-risk zone (above curve). Somalia Federal (0.26) falls in '
         'Brittle Rigidity danger zone; Somalilandia (0.38) in Adaptive Stability optimal zone.')

fig.text(0.5, 0.02, notes, ha='center', fontsize=9, style='italic', wrap=True)

plt.tight_layout()

# Save
plt.savefig('figures/figure3_cli_cultural_matrix.png', dpi=300, bbox_inches='tight')
plt.savefig('figures/figure3_cli_cultural_matrix.pdf', bbox_inches='tight')
print("✅ Figure 3 generated successfully!")
print("   - figures/figure3_cli_cultural_matrix.png (300 DPI)")
print("   - figures/figure3_cli_cultural_matrix.pdf")
plt.close()
