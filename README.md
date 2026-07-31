# Tiger Population Recovery and Forest Cover Dynamics in Nepal (2000–2025)

## Abstract

This repository presents an exploratory quantitative analysis of two coupled conservation trends in Nepal over a 25-year period: (1) national wild tiger (*Panthera tigris tigris*) population recovery, as documented through successive government camera-trap censuses, and (2) national forest cover extent, as reported across multiple independent forest resource assessments and satellite-derived land cover products. The analysis synthesizes publicly available census and remote-sensing data to characterize temporal trends, examine the co-occurrence of tiger population growth and forest cover stability, and provide a reproducible, extensible framework for further geospatial analysis using open-access datasets.

## 1. Background and Motivation

Nepal is internationally recognized as a conservation success story, having nearly quadrupled its wild tiger population between 2009 and 2026 while maintaining relatively stable national forest cover over the same period — a trend that runs counter to deforestation patterns observed in many other tropical and subtropical range states. Nepal's tiger population is concentrated within the Terai Arc Landscape, a transboundary lowland forest corridor spanning Chitwan, Bardiya, Parsa, Banke, and Shuklaphanta National Parks and their surrounding buffer zones and community forests.

This project examines the extent to which national forest cover trends align temporally with tiger population recovery, and situates that relationship within the broader conservation literature, which attributes tiger recovery primarily to anti-poaching enforcement and protected-area management, with community forestry supporting habitat connectivity and quality.

## 2. Repository Contents

| File | Description |
|---|---|
| `Nepal_Tigers_Forest_Cover_2000_2025.ipynb` | Primary analysis notebook (data compilation, visualization, and interpretation) |
| `README.md` | Project documentation (this file) |

## 3. Methods

### 3.1 Data Compilation

Tiger population estimates (2009–2026) were compiled from Nepal's Department of National Parks and Wildlife Conservation (DNPWC) national census releases, cross-referenced against reporting from the Kathmandu Post, IUCN, and Tx2 conservation tracking sources. Pre-2009 figures (2000, 2005) are retained for long-run context but are flagged as pre-camera-trap estimates, methodologically distinct from the systematic censuses conducted from 2009 onward.

Forest cover estimates (1994–2021) were compiled from four independent sources employing different methodologies and sensors:

- National Forest Inventory (aerial photography and field plots)
- Landsat-based national land cover mapping (Uddin et al., 2015)
- Forest Resource Assessment using RapidEye 5m imagery (Department of Forest Research and Survey, 2010–2014)
- Hansen/UMD Global Forest Change dataset (30m Landsat, distributed via Global Forest Watch)

Because these products differ in spatial resolution, forest definition, and reference period, they are treated as **independent point estimates** rather than a harmonized time series, consistent with recommended practice when comparing cross-methodology forest cover products.

### 3.2 Analysis

Data are processed and visualized using `pandas`, `numpy`, and `matplotlib`. Where tiger census years and forest assessment years do not align, linear interpolation is applied strictly for visualization purposes to enable a shared timeline; interpolated values are explicitly distinguished from measured data points in all figures and are not used to support causal claims.

### 3.3 Extension to Live Geospatial Data

The notebook includes template code (Section 5) for extending this analysis using live, internet-accessible geospatial sources:

- Nepal's administrative boundary via OpenStreetMap (`osmnx`)
- The Hansen Global Forest Change dataset (annual tree cover, loss, and gain, 2000–2024) via Google Earth Engine
- Protected area boundaries for the Terai Arc Landscape via the World Database on Protected Areas (WDPA)

These templates were authored in an offline sandbox environment and are provided **unexecuted**; they should be validated by the user prior to use in any downstream analysis.

## 4. Key Findings

- Nepal's national tiger population increased from 121 individuals (2009 census baseline) to 429 individuals (2026 census), a 3.5-fold increase, exceeding the international Tx2 commitment to double tiger populations by 2022.
- Park-level gains between the 2022 and 2026 censuses were recorded in Chitwan, Parsa, Banke, and Shuklaphanta; Bardiya was the sole park to show a population decline over this interval.
- National forest cover estimates across independent assessments range from approximately 39% to 45% of total land area between 1994 and 2021, indicating relative stability rather than net decline.
- Annual tree cover loss reported by Global Forest Watch (e.g., ~4,900 ha in 2025) remains a small fraction of total standing natural forest (~6.5 million ha as of 2020).
- These patterns are consistent with the conservation literature's attribution of tiger recovery to targeted anti-poaching and protected-area interventions, with community forestry (22,000+ Community Forest User Groups managing ~2.9 million ha) contributing to broader habitat and forest cover resilience. The data presented here are descriptive and do not establish a causal relationship between forest cover and tiger population trends.

## 5. Data Sources and Citations

- Department of National Parks and Wildlife Conservation (DNPWC), Nepal — National Tiger Census reports (2009, 2013, 2018, 2022, 2026)
- Global Forest Watch, Nepal Country Dashboard — https://www.globalforestwatch.org/dashboards/country/NPL/
- Hansen, M.C. et al. (2013); Potapov, P. et al. (2022) — Global Forest Change dataset, University of Maryland
- Department of Forest Research and Survey (DFRS) — Forest Resource Assessment 2010–2014, Nepal
- Uddin, K. et al. (2015) — *Development of 2010 national land cover database for Nepal*
- National Forest Inventory 2021, Ministry of Forests and Environment, Government of Nepal
- *Monitoring Forest Cover Trends in Nepal: Insights from 2000–2020*, Sustainability, 17(14), 2025

Full inline citations and source links are provided in the notebook's concluding section.

## 6. Requirements

```bash
pip install pandas numpy matplotlib
```

Optional, for the live geospatial extension in Section 5:

```bash
pip install earthengine-api geemap osmnx
```

Google Earth Engine access requires prior authentication (`ee.Authenticate()`) and an approved GEE account.

## 7. Usage

```bash
jupyter notebook Nepal_Tigers_Forest_Cover_2000_2025.ipynb
```

## 8. Limitations

- Forest cover figures are drawn from methodologically distinct assessments and should not be interpreted as a single continuous measurement series.
- Interpolated values used for shared-timeline visualization are for descriptive purposes only and do not constitute measured data.
- Live geospatial code templates (Section 5) are unexecuted and require independent validation prior to use.
- This analysis is exploratory and descriptive; it is not a peer-reviewed causal or statistical inference study.

## 9. License

License to be determined by the repository maintainer (e.g., MIT for code, CC-BY for written content).

## Acknowledgments

This project was developed as part of the **Environmental Data Science Innovation and Inclusion Lab (ESIIL)** Summer Program, supported by the **U.S. National Science Foundation (NSF)**.

**ESIIL and NSF Project**
