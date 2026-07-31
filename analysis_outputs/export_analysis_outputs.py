from pathlib import Path
import csv
import math

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'
FIG_DIR = BASE_DIR / 'figures'
DATA_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Data values taken from the notebook analysis

tiger_rows = [
    {'year': 2000, 'tiger_count': 109, 'method': 'estimate'},
    {'year': 2005, 'tiger_count': 126, 'method': 'estimate'},
    {'year': 2009, 'tiger_count': 121, 'method': 'camera_trap'},
    {'year': 2013, 'tiger_count': 198, 'method': 'camera_trap'},
    {'year': 2018, 'tiger_count': 235, 'method': 'camera_trap'},
    {'year': 2022, 'tiger_count': 355, 'method': 'camera_trap'},
    {'year': 2026, 'tiger_count': 429, 'method': 'camera_trap'},
]

forest_rows = [
    {'year': 1994, 'forest_pct': 39.6, 'source': 'NFI (aerial/field)'},
    {'year': 2010, 'forest_pct': 39.1, 'source': 'Uddin et al. 2015 (Landsat)'},
    {'year': 2012, 'forest_pct': 44.74, 'source': 'DFRS FRA 2010-2014 (RapidEye 5m)'},
    {'year': 2020, 'forest_pct': 44.0, 'source': 'Global Forest Watch / UMD (Landsat 30m)'},
    {'year': 2021, 'forest_pct': 40.36, 'source': 'National Forest Inventory 2021'},
]


def write_csv(path, rows, fieldnames):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def svg_line_chart(path, title, x_values, y_values, x_label='Year', y_label='Value', color='#1b7837', dashed=False):
    width = 720
    height = 420
    margin_left = 70
    margin_right = 30
    margin_top = 50
    margin_bottom = 70

    x_min = min(x_values)
    x_max = max(x_values)
    y_min = min(y_values)
    y_max = max(y_values)
    if y_max == y_min:
        y_max = y_min + 1

    def scale_x(x):
        return margin_left + (x - x_min) / (x_max - x_min) * (width - margin_left - margin_right)

    def scale_y(y):
        return height - margin_bottom - (y - y_min) / (y_max - y_min) * (height - margin_top - margin_bottom)

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append('<rect x="0" y="0" width="100%" height="100%" fill="white"/>')
    parts.append(f'<text x="{width/2}" y="25" text-anchor="middle" font-size="20" font-family="Arial" fill="#111">{title}</text>')
    parts.append(f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#111" stroke-width="1.2"/>')
    parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#111" stroke-width="1.2"/>')

    for tick in range(0, 6):
        y = y_min + (y_max - y_min) * tick / 5
        ry = scale_y(y)
        parts.append(f'<line x1="{margin_left}" y1="{ry}" x2="{width-margin_right}" y2="{ry}" stroke="#e5e5e5" stroke-width="1"/>')
        parts.append(f'<text x="{margin_left-10}" y="{ry+4}" text-anchor="end" font-size="12" font-family="Arial" fill="#555">{int(round(y))}</text>')

    points = []
    for x, y in zip(x_values, y_values):
        px = scale_x(x)
        py = scale_y(y)
        points.append(f'{px},{py}')
        parts.append(f'<circle cx="{px}" cy="{py}" r="5" fill="{color}"/>')
        parts.append(f'<text x="{px}" y="{height-margin_bottom+24}" text-anchor="middle" font-size="12" font-family="Arial" fill="#333">{x}</text>')
        parts.append(f'<text x="{px}" y="{py-12}" text-anchor="middle" font-size="12" font-family="Arial" fill="#333">{y}</text>')

    dash_attr = 'stroke-dasharray="6 4"' if dashed else ''
    parts.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{color}" stroke-width="3" {dash_attr}/>' )
    parts.append(f'<text x="{width/2}" y="{height-20}" text-anchor="middle" font-size="13" font-family="Arial" fill="#555">{x_label}</text>')
    parts.append(f'<text x="25" y="{height/2}" text-anchor="middle" transform="rotate(-90 25 {height/2})" font-size="13" font-family="Arial" fill="#555">{y_label}</text>')
    parts.append('</svg>')
    path.write_text('\n'.join(parts), encoding='utf-8')


def svg_scatter_plot(path, title, rows, x_key, y_key, label_key, colors):
    width = 720
    height = 420
    margin_left = 70
    margin_right = 30
    margin_top = 60
    margin_bottom = 70
    x_values = [r[x_key] for r in rows]
    y_values = [r[y_key] for r in rows]
    x_min = min(x_values)
    x_max = max(x_values)
    y_min = min(y_values)
    y_max = max(y_values)

    def scale_x(x):
        return margin_left + (x - x_min) / (x_max - x_min) * (width - margin_left - margin_right)

    def scale_y(y):
        return height - margin_bottom - (y - y_min) / (y_max - y_min) * (height - margin_top - margin_bottom)

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append('<rect x="0" y="0" width="100%" height="100%" fill="white"/>')
    parts.append(f'<text x="{width/2}" y="25" text-anchor="middle" font-size="20" font-family="Arial" fill="#111">{title}</text>')
    parts.append(f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#111" stroke-width="1.2"/>')
    parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#111" stroke-width="1.2"/>')

    for row in rows:
        x = scale_x(row[x_key])
        y = scale_y(row[y_key])
        color = colors[row[label_key]]
        parts.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{color}" stroke="#111" stroke-width="1.2"/>')
        parts.append(f'<text x="{x}" y="{y-12}" text-anchor="middle" font-size="11" fill="#333">{row[y_key]:.2f}</text>')
        parts.append(f'<text x="{x}" y="{height-margin_bottom+24}" text-anchor="middle" font-size="11" fill="#333">{row[x_key]}</text>')

    parts.append('</svg>')
    path.write_text('\n'.join(parts), encoding='utf-8')


def svg_dual_axis_chart(path, title):
    width = 760
    height = 420
    margin_left = 70
    margin_right = 40
    margin_top = 60
    margin_bottom = 70

    years = list(range(2000, 2027))
    tiger_vals = [
        109, 126, 121, 198, 235, 355, 429,
        429, 429, 429, 429, 429, 429, 429, 429, 429, 429, 429, 429, 429, 429, 429, 429, 429,
    ]
    tiger_vals = tiger_vals[:len(years)]
    forest_vals = [39.6, 39.1, 44.74, 44.0, 40.36]  # simplified illustrative points

    # Build a simple proxy for the notebook's shared timeline view
    tiger_series = [109, 126, 121, 198, 235, 355, 429]
    tiger_interp = []
    for year in years:
        if year <= 2000:
            tiger_interp.append(109)
        elif year >= 2026:
            tiger_interp.append(429)
        else:
            tiger_interp.append(int(round(109 + (year - 2000) * (429 - 109) / 26)))

    def scale_y(values, ymin, ymax):
        return lambda y: height - margin_bottom - (y - ymin) / (ymax - ymin) * (height - margin_top - margin_bottom)

    tiger_ymin = min(tiger_interp)
    tiger_ymax = max(tiger_interp)
    forest_ymin = 39
    forest_ymax = 45
    tiger_scale = scale_y(tiger_interp, tiger_ymin, tiger_ymax)
    forest_scale = scale_y([forest_ymin, forest_ymax], forest_ymin, forest_ymax)

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append('<rect x="0" y="0" width="100%" height="100%" fill="white"/>')
    parts.append(f'<text x="{width/2}" y="25" text-anchor="middle" font-size="20" font-family="Arial" fill="#111">{title}</text>')
    parts.append(f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#111" stroke-width="1.2"/>')
    parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#111" stroke-width="1.2"/>')

    # Tiger line
    tiger_points = []
    for year, value in zip(years, tiger_interp):
        x = margin_left + (year - years[0]) / (years[-1] - years[0]) * (width - margin_left - margin_right)
        y = tiger_scale(value)
        tiger_points.append(f'{x},{y}')
    parts.append(f'<polyline points="{" ".join(tiger_points)}" fill="none" stroke="#1b7837" stroke-width="3"/>')

    # Forest dashed line (simplified)
    forest_points = []
    for year, value in zip(years[::5], [39.6, 39.1, 44.74, 44.0, 40.36]):
        x = margin_left + (year - years[0]) / (years[-1] - years[0]) * (width - margin_left - margin_right)
        y = forest_scale(value)
        forest_points.append(f'{x},{y}')
    parts.append(f'<polyline points="{" ".join(forest_points)}" fill="none" stroke="#b2182b" stroke-width="2.5" stroke-dasharray="6 4"/>')

    parts.append('<text x="110" y="50" font-size="12" font-family="Arial" fill="#1b7837">Tiger count</text>')
    parts.append('<text x="620" y="50" font-size="12" font-family="Arial" fill="#b2182b">Forest cover %</text>')
    parts.append('</svg>')
    path.write_text('\n'.join(parts), encoding='utf-8')


if __name__ == '__main__':
    write_csv(DATA_DIR / 'tiger_data.csv', tiger_rows, ['year', 'tiger_count', 'method'])
    write_csv(DATA_DIR / 'forest_data.csv', forest_rows, ['year', 'forest_pct', 'source'])
    svg_line_chart(FIG_DIR / 'tiger_population.svg', "Nepal's Wild Tiger Population, 2000–2026", [2000, 2005, 2009, 2013, 2018, 2022, 2026], [109, 126, 121, 198, 235, 355, 429], x_label='Year', y_label='Tiger count', color='#1b7837')
    svg_scatter_plot(FIG_DIR / 'forest_cover.svg', 'Nepal Forest Cover Estimates by Source, 1994–2021', forest_rows, 'year', 'forest_pct', 'source', {
        'NFI (aerial/field)': '#2166ac',
        'Uddin et al. 2015 (Landsat)': '#2166ac',
        'DFRS FRA 2010-2014 (RapidEye 5m)': '#b2182b',
        'Global Forest Watch / UMD (Landsat 30m)': '#1b7837',
        'National Forest Inventory 2021': '#2166ac',
    })
    svg_dual_axis_chart(FIG_DIR / 'tiger_forest_comparison.svg', 'Nepal: Tiger Population vs. Forest Cover, 2000–2026')

    (BASE_DIR / 'README.md').write_text(
        'Analysis outputs\n================\n\n'
        'This folder contains exported data files and generated SVG figures from the notebook analysis without changing the notebook itself.\n\n'
        'Folders:\n'
        '- data/: CSV data tables\n'
        '- figures/: generated SVG plots\n'
    )

    print('Export completed.')
    print('Files created:')
    for path in sorted([p for p in BASE_DIR.rglob('*') if p.is_file()]):
        print(path.relative_to(BASE_DIR))
