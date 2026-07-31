# Nepal Tigers & Forest Cover (2000–2025)

A Jupyter notebook exploring two intertwined Nepali conservation stories over the past ~25 years:

1. **Tiger population recovery** — national census counts from 2000 to 2026
2. **Forest cover change** — national forest extent from government assessments and global remote-sensing data

The notebook overlays both trends, checks their correlation (with honest caveats), and includes ready-to-run templates for pulling live satellite data (Hansen/Global Forest Change via Google Earth Engine, Nepal's boundary via OpenStreetMap).

## Contents

- `Nepal_Tigers_Forest_Cover_2000_2025.ipynb` — the main analysis notebook

## What's in the notebook

| Section | Description |
|---|---|
| 1. Tiger population data | National tiger census counts (2009–2026), sourced from DNPWC census releases |
| 2. Forest cover data | Forest cover % estimates from NFI, DFRS/FRA, Uddin et al. 2015, and Global Forest Watch |
| 3. Combined analysis | Dual-axis chart of tiger count vs. forest cover, plus a correlation check |
| 4. Key findings | Summary of the main takeaways |
| 5. Live data templates | Optional Earth Engine / OSM code to pull real Hansen Global Forest Change rasters (requires internet + GEE auth — not run in this repo's committed outputs) |
| 6. Sources | Full citation list |

## Key findings

- Nepal's wild tiger population rose from **121 (2009)** to **429 (2026)** — a **3.5x increase**, exceeding the international Tx2 commitment to double tiger numbers by 2022.
- National forest cover estimates cluster around **39–45%** of land area from 1994–2021, depending on methodology — broadly stable rather than declining.
- Community forestry (22,000+ Community Forest User Groups managing ~2.9M hectares) is widely credited as a key driver of forest cover resilience.
- Tiger recovery is attributed mainly to anti-poaching enforcement and protected-area management — the notebook is careful not to overstate a causal link to forest cover alone.

## Data sources

- Nepal DNPWC national tiger census results (2009, 2013, 2018, 2022, 2026)
- [Global Forest Watch — Nepal country dashboard](https://www.globalforestwatch.org/dashboards/country/NPL/)
- Hansen et al. 2013 / Potapov et al. 2022, Global Forest Change dataset (UMD)
- Department of Forest Research and Survey (DFRS), Forest Resource Assessment 2010–2014
- Uddin, K. et al. 2015, *Development of 2010 national land cover database for Nepal*
- National Forest Inventory 2021, Government of Nepal
- *Monitoring Forest Cover Trends in Nepal: Insights from 2000–2020*, Sustainability, 2025

Full citations with URLs are in the notebook's final section.

## Requirements

```bash
pip install pandas numpy matplotlib
```

To run Section 5 (optional live geospatial pull), also install:

```bash
pip install earthengine-api geemap osmnx
```

and authenticate with `ee.Authenticate()` (requires a Google Earth Engine account).

## Usage

```bash
jupyter notebook Nepal_Tigers_Forest_Cover_2000_2025.ipynb
```

## Notes & limitations

- Forest cover figures come from different measurement methods (aerial inventory vs. Landsat vs. RapidEye) and are **not a single continuous time series** — compare trends within a source, not point-to-point across sources.
- The dual-axis correlation chart uses linear interpolation to align mismatched measurement years for visualization only; interpolated points are clearly marked and shouldn't be read as measured data.
- Section 5's Earth Engine templates are commented out and untested in this repo, since the authoring environment had no internet access — verify them yourself before relying on their output.

## License

Add a license of your choice (e.g. MIT) if you plan to share this publicly.
