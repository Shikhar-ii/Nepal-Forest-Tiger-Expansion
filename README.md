# Tiger Recovery and Forest Cover in Nepal

## Overview

This repository now combines a data analysis notebook, exported figures, and a polished web page to present a clear conservation comparison:

- Tiger numbers increased strongly from 121 to 429.
- Forest cover remained broadly stable at roughly 39–45%.
- The habitat challenge is not simply about total forest area; it is also about whether the remaining forests are sufficiently connected, protected, and suitable for continued tiger expansion.

The updated website highlights this message with a clearer time series, a park-level comparison, and an OpenStreetMap-style habitat map.

## Repository contents

- [index.html](index.html) — research-style landing page for the story
- [script.js](script.js) — custom SVG charts for tiger growth, park changes, and forest-cover interpretation
- [styles.css](styles.css) — presentation styling for the page
- [Nepal_Tigers_Forest_Cover_2000_2025.ipynb](Nepal_Tigers_Forest_Cover_2000_2025.ipynb) — main analysis notebook
- [analysis_outputs/export_analysis_outputs.py](analysis_outputs/export_analysis_outputs.py) — exports improved SVG figures into the analysis_outputs folder

## Main message

Nepal’s tiger recovery is a genuine conservation success, but the story should be presented carefully. The forest base is not collapsing, yet it is still relatively limited and fragmented enough that habitat quality and connectivity remain important constraints for future growth.

## How to view the site

Open [index.html](index.html) in a browser, or serve the folder locally with a simple web server.

```bash
python3 -m http.server 8000
```

Then visit http://localhost:8000/.
