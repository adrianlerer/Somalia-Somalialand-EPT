# FIGURES DOCUMENTATION - Somalia/Somalilandia CLI Paper

**Date Generated**: November 21, 2025  
**Software**: Python 3.12.11 with matplotlib, numpy, scipy  
**Resolution**: 300 DPI (publication-quality)  
**Formats**: PDF (vector) + PNG (raster)

---

## FIGURE 1: TIMELINE VISUALIZATION (MANDATORY)

### File Locations
- **Vector PDF**: `/figures/figure1_timeline.pdf` (44 KB)
- **Raster PNG**: `/figures/figure1_timeline.png` (618 KB, 300 DPI)
- **Source Code**: `/scripts/figure1_timeline.py` (8,090 characters)

### Specifications
- **Dimensions**: 14" × 8" (landscape orientation)
- **Timeline Range**: 1960-2024 (64 years)
- **Tracks**: 2 parallel (Somalia Federal, Somalilandia)
- **Events Marked**: 15 total (3 common baseline + 7 Somalia + 5 Somalilandia)

### Visual Elements
**Color Coding**:
- Common baseline (1960-1991): Gray shading (alpha 0.15)
- 1991 exogenous shock: Red dashed vertical line
- Somalia Federal track: Red (#d62728) with square markers
- Somalilandia track: Blue (#1f77b4) with triangle markers

**Event Markers**:
- Common events (1960-1991): Black circles with yellow text boxes
- Somalia Federal: Red squares with light red (#ffcccc) text boxes
- Somalilandia: Blue triangles with light blue (#cce5ff) text boxes

**Key Annotations** (4):
1. "CRITICAL JUNCTURE: Exogenous shock creates natural experiment" (1991, red)
2. "Somalilandia: Bottom-up legitimacy (97.1% referendum)" (2001, blue)
3. "Somalia: Top-down rigidity (provisional constitution 13 years)" (2012, red)
4. "Outcomes Divergence: FH 43.7 vs 8 (6x), Deaths 40 vs 3,116/year (78x)" (2024, black)

### Data Sources
- Constitutional events: TASK_FACTCHECK_CONSTITUTIONAL_EVENTS.md (93.3% verified)
- Historical context: Lewis (2002), Bradbury (2008)
- CLI scores: Appendix A calculations
- Governance outcomes: Freedom House (2024), UCDP/ACLED (2015-2024)

---

### Publication-Ready Caption

**Figure 1. Natural Experiment Timeline: Somalia Federal vs Somalilandia Constitutional Divergence (1960-2024)**

The 1991 state collapse created an exogenous shock enabling divergent constitutional paths despite common baseline (1960-1991 Barre regime). Somalia Federal adopted rigid top-down institutions (CLI 0.76): 4.5 clan formula (2000-present, 0 amendments), provisional constitution (2012-present, 13 years without finalization), no direct elections (1969-2024). Somalilandia pursued flexible bottom-up constitutionalism (CLI 0.54): Borama/Hargeisa conferences (1993-1997), referendum legitimacy (2001, 97.1% approval, 99.9% turnout), direct elections (2003-2024), peaceful opposition victories (2010, 2021, 2024). By 2024, outcomes diverged: Somalilandia Freedom House score 6x higher (43.7 vs 8), conflict deaths 78x lower (~40 vs ~3,116 annually), demonstrating CLI correlation with governance quality.

**Sources**: Lewis (2002); Bradbury (2008); Federal Republic of Somalia (2012); Republic of Somalilandia (2001); Freedom House (2024); UCDP/ACLED (2015-2024); author compilation.

---

## FIGURE 2: CLI vs OUTCOMES SCATTERPLOTS (OPTIONAL)

### File Locations
- **Vector PDF**: `/figures/figure2_scatterplots.pdf` (37 KB)
- **Raster PNG**: `/figures/figure2_scatterplots.png` (472 KB, 300 DPI)
- **Source Code**: `/scripts/figure2_scatterplots.py` (6,952 characters)

### Specifications
- **Dimensions**: 14" × 6" (landscape, two-panel layout)
- **Panel A**: CLI (x-axis 0.50-0.80) vs Freedom House Score (y-axis 0-50)
- **Panel B**: CLI (x-axis 0.50-0.80) vs Log₁₀(Annual Deaths) (y-axis 1.4-3.6)

### Data Values

| Entity | CLI | Freedom House | Annual Deaths | Log₁₀(Deaths) |
|--------|-----|---------------|---------------|---------------|
| **Somalia Federal** | 0.76 | 8 | 3,116 | 3.49 |
| **Somalilandia** | 0.54 | 43.7 | 40 | 1.60 |

### Statistical Results
- **Panel A Correlation**: r = -1.00 (perfect negative correlation, N=2)
  - Lower CLI → Higher democracy
  - Somalia: CLI 0.76 → FH 8
  - Somalilandia: CLI 0.54 → FH 43.7 (6x higher)
  
- **Panel B Correlation**: r = +1.00 (perfect positive correlation, N=2)
  - Lower CLI → Lower violence
  - Somalia: CLI 0.76 → 3,116 deaths/year
  - Somalilandia: CLI 0.54 → 40 deaths/year (78x lower)

### Visual Elements
**Color Coding**:
- Somalia Federal: Red (#d62728)
- Somalilandia: Blue (#1f77b4)
- Trendlines: Gray dashed lines

**Annotations**:
- Correlation coefficients: Yellow boxes with "r = ±1.00, N=2"
- Interpretation boxes: Light red "Higher CLI → Lower democracy" / "Higher CLI → Higher violence"
- Death counts: Color-coded text labels (3,116 vs 40 deaths/year)

### Methodological Note
Perfect correlations (r = ±1.00) are **artifacts of N=2 natural experiment design**, not universal laws. These correlations demonstrate that CLI predictions hold in this specific paired comparison but require replication across additional cases (e.g., Latin America CLI studies) to establish generalizability.

---

### Publication-Ready Caption

**Figure 2. Constitutional Lock-In Index (CLI) Correlates with Governance Outcomes**

Panel A: Lower CLI predicts higher Freedom House democracy scores (r = -1.00, N=2). Somalilandia's flexible institutions (CLI 0.54) achieve 6x higher score (43.7) than Somalia Federal's rigid system (CLI 0.76, score 8). Panel B: Lower CLI predicts lower conflict intensity (r = +1.00, N=2). Somalilandia experiences 78x fewer annual deaths (~40) than Somalia Federal (~3,116), measured 2015-2024.

**Methodological Note**: Perfect correlations (r = ±1.00) are artifacts of N=2 natural experiment design, not universal laws. Correlations demonstrate CLI predictions hold in this paired comparison but require replication across additional cases (e.g., Latin America CLI studies) to establish generalizability. Log transformation applied to conflict deaths to normalize skewed distribution.

**Sources**: Author CLI calculations; Freedom House (2024); UCDP/ACLED (2015-2024).

---

## REPLICATION INSTRUCTIONS

### Software Requirements
```bash
# Python 3.12+ with required packages
pip3 install matplotlib seaborn pandas numpy scipy
```

### Generate Figures
```bash
# Navigate to project directory
cd /home/user/webapp/papers/drafts/somalia_somalilandia_ept

# Generate Figure 1 (Timeline)
python3 scripts/figure1_timeline.py

# Generate Figure 2 (Scatterplots)
python3 scripts/figure2_scatterplots.py
```

### Output Locations
- Figures saved to: `/figures/` directory
- PDF (vector): Preferred for LaTeX/journal submission
- PNG (raster): Alternative for Word/PowerPoint

### Customization Options
**Figure 1**:
- Edit event positions: Modify `somalia_events` and `somalilandia_events` lists
- Adjust colors: Change `somalia_color` and `somalilandia_color` variables
- Timeline range: Modify `years` array and `ax.set_xlim()`

**Figure 2**:
- Data values: Edit `cli_scores`, `fh_scores`, `annual_deaths` arrays
- Panel layout: Adjust `plt.rcParams['figure.figsize']` tuple
- Axis ranges: Modify `ax1.set_xlim()`, `ax1.set_ylim()`, etc.

---

## PUBLICATION CHECKLIST

### Figure 1 (Timeline)
- ✅ 300 DPI resolution (publication-quality)
- ✅ Vector PDF format (preferred for journals)
- ✅ High-resolution PNG (alternative format)
- ✅ Color-blind safe palette (red/blue distinguishable)
- ✅ Clear event labels (readable at 10-12pt)
- ✅ Legend included (4 elements)
- ✅ Caption text provided (250 words)
- ✅ Sources cited (7 references)

### Figure 2 (Scatterplots)
- ✅ 300 DPI resolution (publication-quality)
- ✅ Vector PDF format (preferred for journals)
- ✅ High-resolution PNG (alternative format)
- ✅ Two-panel layout (side-by-side)
- ✅ Statistical annotations (r values, N=2)
- ✅ Methodological note (N=2 caveat)
- ✅ Caption text provided (150 words)
- ✅ Sources cited (3 references)

---

## INTEGRATION WITH MAIN TEXT

### Section 3: Historical Evolution
**Reference**: "See Figure 1 for complete constitutional events timeline (1960-2024)."  
**Location**: After discussing 1991 exogenous shock and divergent paths.

### Section 5: Empirical Findings
**Reference**: "Figure 2 demonstrates perfect correlations (r = ±1.00) between CLI and governance outcomes."  
**Location**: After presenting Freedom House scores and conflict death statistics.

### Section 6: Robustness
**Reference**: "Figure 2 methodological note acknowledges N=2 limitation requiring replication."  
**Location**: Limitations subsection discussing generalizability.

### Section 7: Policy Implications
**Reference**: "Figure 1 illustrates the stark divergence in constitutional design choices post-1991."  
**Location**: Constitutional design recommendations subsection.

---

## TECHNICAL SPECIFICATIONS

### Figure 1 Technical Details
- **Software**: Python 3.12.11 + matplotlib 3.9.2
- **Font**: Serif (publication standard)
- **Line widths**: 1.5-3.0 points (axes/lines)
- **Marker sizes**: 8-12 points (events)
- **Text boxes**: Rounded corners, alpha 0.7-0.9
- **Grid**: Dashed lines, alpha 0.3
- **File size**: 44 KB (PDF), 618 KB (PNG)

### Figure 2 Technical Details
- **Software**: Python 3.12.11 + matplotlib 3.9.2 + scipy 1.14.1
- **Font**: Serif (publication standard)
- **Marker sizes**: 200 points (large, visible)
- **Trendlines**: Dashed gray, linewidth 2.0
- **Regression**: scipy.stats.linregress (linear OLS)
- **Log transformation**: numpy.log10 (base-10 logarithm)
- **File size**: 37 KB (PDF), 472 KB (PNG)

---

## DESIGN RATIONALE

### Figure 1: Timeline Choice
**Why horizontal timeline?**
- Clear chronological progression (left to right)
- Allows parallel tracks for direct comparison
- Space for detailed event annotations
- Standard in political science/history journals

**Why 1960 start date?**
- Independence year (common baseline begins)
- Establishes pre-treatment period (1960-1991)
- Shows 64-year arc (meaningful historical scope)

**Why 1991 exogenous shock emphasis?**
- Critical juncture for natural experiment validity
- Visual separation of common vs divergent periods
- Red color draws attention to treatment assignment

### Figure 2: Scatterplot Choice
**Why two-panel layout?**
- Shows CLI correlation with TWO distinct outcomes (democracy + violence)
- Side-by-side comparison highlights dual mechanism validation
- Efficient use of space (one figure number)

**Why log transformation (Panel B)?**
- Deaths data highly skewed (3,116 vs 40 = 78x ratio)
- Log scale normalizes distribution
- Linear regression more appropriate on log scale
- Common practice in violence research

**Why include N=2 caveat?**
- Methodological transparency (perfect r = ±1.00 is artifact)
- Avoids overstating generalizability
- Acknowledges natural experiment limitation
- Directs readers to future replication studies

---

## FILE MANIFEST

### Generated Files (4)
1. `/figures/figure1_timeline.pdf` - Vector timeline (44 KB)
2. `/figures/figure1_timeline.png` - Raster timeline (618 KB, 300 DPI)
3. `/figures/figure2_scatterplots.pdf` - Vector scatterplots (37 KB)
4. `/figures/figure2_scatterplots.png` - Raster scatterplots (472 KB, 300 DPI)

### Source Code (2)
1. `/scripts/figure1_timeline.py` - Timeline generation script (8,090 chars)
2. `/scripts/figure2_scatterplots.py` - Scatterplot generation script (6,952 chars)

### Documentation (1)
1. `/docs/FIGURES_DOCUMENTATION.md` - This file

**Total Size**: ~1.2 MB (all files)

---

## USAGE RECOMMENDATIONS

### For SSRN Working Paper
- **Use PNG format** (618 KB, 472 KB) for easy embedding in Word/PDF
- Include both figures in main text (not appendices)
- Figure 1: After Section 3 (Historical Evolution)
- Figure 2: After Section 5 (Empirical Findings)

### For Journal Submission
- **Use PDF format** (44 KB, 37 KB) for vector graphics
- Submit as separate files (figure1.pdf, figure2.pdf)
- Reference in manuscript: "See Figure 1" / "See Figure 2"
- Include captions in manuscript (not embedded in figures)

### For Presentations
- **Use PNG format** (higher compatibility with PowerPoint/Keynote)
- Consider enlarging font sizes for projection (current: 10-12pt)
- May need to simplify annotations for slide format

---

**END OF FIGURES DOCUMENTATION**

**Date**: November 21, 2025  
**Status**: ✅ COMPLETE (2 figures, 4 files, publication-ready)  
**Next Step**: Integrate figures into main manuscript, update PROJECT_TRACKING.md
