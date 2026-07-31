# Nepal Tiger Recovery & Forest Cover — Research Story

**Live site:** [nepal-forest-tiger-expansion.vercel.app](https://nepal-forest-tiger-expansion.vercel.app)

A data-driven research project examining Nepal's wild tiger population recovery (2000–2026) alongside national forest-cover trends, presented as an interactive web story, a reproducible Jupyter notebook, a conference-style research paper, and a slide deck.

## Overview

Nepal's wild tiger population grew 3.5x from a 2009 baseline of 121 individuals to 429 in 2026, while independent national forest assessments place forest cover in a stable 39–45% range over the same period — a trend at odds with the deforestation seen across much of the tropics. This repository compiles publicly available census and remote-sensing data to document that trend, generates the supporting figures and maps from scratch in Python, and packages the findings for three audiences: a general web reader, a technical/reproducibility audience, and an academic one.

## Live Site

The site at [nepal-forest-tiger-expansion.vercel.app](https://nepal-forest-tiger-expansion.vercel.app) presents the research story with:

- A hero section summarizing headline figures (3.5x population growth, 39–45% stable forest cover, Terai corridor context)
- A combined tiger-population / forest-cover trend chart
- A park-level tiger change comparison (2022 → 2026 census)
- An OpenStreetMap-backed habitat map of the Terai Arc Landscape

Built with plain HTML/CSS/JS (`index.html`, `styles.css`, `script.js`), with all chart and map imagery generated from data rather than stock images or placeholders.

## Repository Structure

```
├── index.html                              # Web research story (deployed via Vercel)
├── styles.css                              # Site styling
├── script.js                               # Page interactions (particle/tilt effects) + image rendering
├── analysis_outputs/
│   ├── export_analysis_outputs.py          # Regenerates all figures from repository CSV data
│   └── figures/
│       ├── tiger_forest_timeline.svg       # Combined tiger population / forest cover time series
│       ├── park_change.svg                 # Park-level tiger change bar chart
│       └── habitat_map.png                 # OpenStreetMap-based Terai habitat & park overview
├── Nepal_Tigers_Forest_Cover_2000_2025.ipynb   # Reproducible analysis notebook
├── Nepal_Tigers_Forest_Cover_Paper.docx        # Full research paper (LNCS-style formatting)
├── Nepal_Tigers_Forest_Cover_Presentation.pptx # Slide deck summary
├── LICENSE                                 # MIT
└── README.md
```

## Regenerating the Figures

The site's figures are not static assets — they're generated from the repository's underlying data using Python:

```bash
python3 -m pip install pandas matplotlib geopandas osmnx contextily shapely
python3 analysis_outputs/export_analysis_outputs.py
```

This reads the repository's CSV data and rewrites everything under `analysis_outputs/figures/`, including the OpenStreetMap-derived habitat map (via `osmnx`/`contextily`) and the two chart SVGs (via `matplotlib`). Re-run it after updating any source data, then refresh `index.html` in a browser to see the changes reflected.

## Key Findings

| Metric | Value |
|---|---|
| Tiger population growth (2009 → 2026) | 3.5x (121 → 429) |
| Tx2 goal (double tigers by 2022) | Exceeded, four years ahead of schedule |
| National forest cover range (1994–2021) | 39–45%, stable across independent assessments |
| Parks gaining tigers (2022 → 2026) | 4 of 5 (Chitwan, Parsa, Banke, Shuklaphanta); Bardiya declined |
| Global context | Nepal's growth rate outpaces every other tiger-range country in relative terms |

Full methodology, global comparisons, and discussion of the government programs (Terai Arc Landscape Program, community forestry, anti-poaching enforcement) behind this recovery are in the notebook and paper.

## Other Deliverables

- **`Nepal_Tigers_Forest_Cover_2000_2025.ipynb`** — the underlying data compilation, charts, and descriptive correlation analysis, with citations for every figure used.
- **`Nepal_Tigers_Forest_Cover_Paper.docx`** — a full write-up (introduction, background, methods, results, discussion, references) situating Nepal's recovery in global tiger-conservation trends.
- **`Nepal_Tigers_Forest_Cover_Presentation.pptx`** — a short slide deck version for presentations.

## Data Sources

- Department of National Parks and Wildlife Conservation (DNPWC), Nepal — National Tiger Census releases (2009–2026)
- Global Forest Watch / Hansen Global Forest Change dataset (University of Maryland)
- Department of Forest Research and Survey (DFRS) — Forest Resource Assessment 2010–2014
- National Forest Inventory 2021, Government of Nepal
- Global Tiger Forum / WWF range-country population estimates
- OpenStreetMap (habitat map basemap)

Full citations are listed in the notebook and paper.

## Limitations

- Forest-cover figures come from methodologically distinct assessments (aerial inventory, Landsat, RapidEye) and are not a single continuous time series.
- Pre-2009 tiger figures are pre-camera-trap estimates, not directly comparable to later systematic censuses.
- Correlations shown between tiger population and forest cover are descriptive, not causal.

## Acknowledgments

Developed as part of the **ESIIL**, University of Colorado Boulder, supported by the **U.S. National Science Foundation (NSF)**.

**Author:** Shikhar Pandey
**Mentor:** Nate Quarderer, ESIIL Education Director

## License

MIT — see [`LICENSE`](./LICENSE).
