# Nepal Tiger Recovery and Forest Cover Dynamics (2000–2026)

> **An open, reproducible research project analyzing Nepal's tiger population recovery alongside long-term forest-cover trends through interactive visualization, geospatial analysis, and reproducible computational workflows.**

**Live Research Story:** https://nepal-forest-tiger-expansion.vercel.app

---

## Abstract

Nepal represents one of the world's most significant wildlife conservation success stories. Between the first nationwide camera-trap census in 2009 and the 2026 national census, the country's wild tiger population increased from **121 to 429 individuals**, exceeding the international **Tx2** conservation target while many tropical regions continued experiencing biodiversity loss.

This project integrates publicly available wildlife census data, national forest inventories, satellite-derived forest-cover assessments, and geospatial habitat information into a fully reproducible research pipeline. The repository combines scientific analysis, interactive visualization, and academic reporting to examine how long-term forest stability coincides with one of the fastest documented tiger recoveries globally.

Rather than serving only as a visualization website, this repository provides an end-to-end reproducible research workflow, enabling readers to regenerate figures, inspect methodology, reproduce analyses, and explore the underlying datasets.

---

# Research Contributions

This project contributes:

- A reproducible compilation of Nepal's national tiger census data spanning 2000–2026
- Integration of independent national forest-cover assessments into a unified longitudinal dataset
- Automated generation of publication-quality figures directly from source data
- Geospatial visualization of protected habitats within Nepal's Terai Arc Landscape
- An interactive research narrative designed to improve accessibility of conservation data
- A conference-style research paper documenting methodology, analysis, findings, and limitations
- A fully reproducible Jupyter notebook allowing independent verification of results

---

# Key Findings

| Finding | Result |
|----------|--------|
| Tiger population growth | **121 → 429 (2009–2026)** |
| Population increase | **3.5× growth** |
| Tx2 Conservation Target | **Exceeded four years ahead of schedule** |
| Forest-cover trend | **Stable (~39–45%) across national assessments** |
| Protected areas increasing tiger populations | **4 of 5 major parks** |
| Global significance | **Highest proportional tiger recovery among range countries** |

---

# Research Questions

This project investigates:

1. How has Nepal's tiger population changed over the past two decades?
2. How has national forest cover changed during the same period?
3. Can publicly available conservation datasets be integrated into a reproducible computational workflow?
4. How can interactive visualization improve communication of ecological research?

---

# Repository Structure

```
.
├── index.html
├── styles.css
├── script.js
│
├── analysis_outputs/
│   ├── export_analysis_outputs.py
│   └── figures/
│       ├── tiger_forest_timeline.svg
│       ├── park_change.svg
│       └── habitat_map.png
│
├── Nepal_Tigers_Forest_Cover_2000_2025.ipynb
├── Nepal_Tigers_Forest_Cover_Paper.docx
├── Nepal_Tigers_Forest_Cover_Presentation.pptx
├── LICENSE
└── README.md
```

---

# Components

## 1. Interactive Research Story

The deployed website presents the research through an interactive narrative featuring:

- Executive summary of principal findings
- Population and forest-cover time series
- Park-level census comparisons
- Interactive habitat mapping
- Responsive visual storytelling
- Data-driven graphics generated directly from source datasets

---

## 2. Reproducible Analysis

The accompanying Jupyter notebook documents every analytical step, including:

- Data preprocessing
- Dataset integration
- Statistical summaries
- Figure generation
- Correlation analysis
- Source citations
- Reproducible workflows

All visualizations included in the website and paper originate from notebook-generated outputs.

---

## 3. Geospatial Analysis

The project incorporates open geospatial datasets to visualize:

- Protected areas
- Major tiger habitats
- Terai Arc Landscape
- Habitat connectivity
- OpenStreetMap basemap integration

using:

- GeoPandas
- OSMnx
- Contextily
- Shapely

---

## 4. Research Paper

The repository includes a conference-style research manuscript containing:

- Introduction
- Background
- Literature review
- Methodology
- Results
- Discussion
- Limitations
- References

---

## 5. Presentation

A presentation deck summarizes the research for conference talks, classroom presentations, and outreach activities.

---

# Reproducing the Analysis

Install dependencies

```bash
pip install pandas matplotlib geopandas osmnx contextily shapely
```

Generate all figures

```bash
python analysis_outputs/export_analysis_outputs.py
```

The script automatically recreates:

- Tiger population timeline
- Forest-cover timeline
- Protected-area comparison chart
- Habitat map

from the repository's source datasets.

---

# Technologies

### Programming

- Python
- HTML
- CSS
- JavaScript

### Data Analysis

- Pandas
- NumPy
- Matplotlib

### Geospatial

- GeoPandas
- OSMnx
- Contextily
- Shapely

### Visualization

- SVG
- Interactive Web Components
- Responsive Design

---

# Data Sources

The analysis synthesizes publicly available information from:

- Department of National Parks and Wildlife Conservation (DNPWC)
- Department of Forest Research and Survey (DFRS)
- National Forest Inventory (Government of Nepal)
- Global Forest Watch
- Hansen Global Forest Change Dataset (University of Maryland)
- WWF
- Global Tiger Forum
- OpenStreetMap

Complete citations are available in the notebook and research paper.

---

# Methodological Notes

The project prioritizes transparency and reproducibility.

Key considerations include:

- Forest-cover estimates originate from independent national assessments using different remote-sensing methodologies.
- Tiger estimates prior to the adoption of nationwide camera-trap surveys are not directly comparable with later census data.
- Reported relationships between forest cover and tiger populations are descriptive and should not be interpreted as causal.

---

# Research Impact

This project demonstrates how open ecological datasets can be transformed into reproducible scientific products that serve multiple audiences simultaneously:

- Researchers seeking transparent workflows
- Conservation practitioners
- Policy makers
- Students
- General public

By integrating computational analysis, geospatial visualization, scientific writing, and interactive storytelling, the repository illustrates a reproducible approach for communicating conservation science.

---

# Acknowledgments

Developed during the **(ESIIL)** at the **University of Colorado Boulder**.

Supported by the **U.S. National Science Foundation (NSF).**

**Author**

**Shikhar Pandey**

**Mentor**

**Nate Quarderer**  
Education Director, ESIIL

---

# Citation

If you use this repository, figures, or analysis in academic work, please cite:

```
Pandey, S. (2026).
Nepal Tiger Recovery and Forest Cover Dynamics (2000–2026):
A Reproducible Computational Analysis.
GitHub Repository.
ESIIL & NSF FUNDED
```

---

# License

This project is released under the **MIT License**.
