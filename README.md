# Tiger Recovery and Forest Cover in Nepal

This repository now uses Python-generated figures and an OpenStreetMap-backed habitat map to present a polished conservation story for Nepal.

## What changed

- `analysis_outputs/export_analysis_outputs.py` now reads repository CSV data and generates real chart graphics using `pandas`, `matplotlib`, `geopandas`, `osmnx`, and `contextily`.
- `index.html` now displays actual exported figures from `analysis_outputs/figures/` instead of placeholder visuals.
- `styles.css` was updated to support the new research-style figures and map layout.
- `script.js` now preserves the page's animated particle and tilt interaction while relying on real generated image content.

## Generated figures

- `analysis_outputs/figures/tiger_forest_timeline.svg` — combined tiger population and forest cover time series
- `analysis_outputs/figures/park_change.svg` — park-level tiger change bar chart
- `analysis_outputs/figures/habitat_map.png` — OpenStreetMap-based habitat and park overview

## How to regenerate

Install the required Python packages and run the export script:

```bash
python3 -m pip install pandas matplotlib geopandas osmnx contextily shapely
python3 analysis_outputs/export_analysis_outputs.py
```

Then open `index.html` in a browser to review the updated research visuals.
