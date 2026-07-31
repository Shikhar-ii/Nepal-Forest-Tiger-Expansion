from pathlib import Path
import csv

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

park_rows = [
    {'park': 'Chitwan', 'change': 17},
    {'park': 'Parsa', 'change': 30},
    {'park': 'Banke', 'change': 26},
    {'park': 'Shuklaphanta', 'change': 14},
    {'park': 'Bardiya', 'change': -13},
]


def write_csv(path, rows, fieldnames):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def svg_line_chart(path, title, x_values, y_values, color='#2f6f4f'):
    width = 760
    height = 460
    margin_left = 80
    margin_right = 90
    margin_top = 70
    margin_bottom = 90

    x_min = min(x_values)
    x_max = max(x_values)
    tiger_min = 100
    tiger_max = 450
    forest_min = 39
    forest_max = 45

    def scale_x(x):
        return margin_left + (x - x_min) / (x_max - x_min) * (width - margin_left - margin_right)

    def scale_tiger(y):
        return height - margin_bottom - (y - tiger_min) / (tiger_max - tiger_min) * (height - margin_top - margin_bottom)

    def scale_forest(y):
        return height - margin_bottom - (y - forest_min) / (forest_max - forest_min) * (height - margin_top - margin_bottom)

    def tick_values(start, end, steps):
        return [round(start + (end - start) * i / steps, 1) for i in range(steps + 1)]

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append('<rect x="0" y="0" width="100%" height="100%" fill="#f7fbf4"/>')
    parts.append('<rect x="22" y="22" width="716" height="416" rx="18" fill="#ffffff" stroke="#dfead8" stroke-width="1.5"/>')
    parts.append(f'<text x="{width/2}" y="44" text-anchor="middle" font-size="20" font-family="Arial" fill="#183d2b" font-weight="700">{title}</text>')
    parts.append('<text x="80" y="58" font-size="12" font-family="Arial" fill="#4b5563">Tiger recovery outpaced the forest base, underscoring the need for habitat connectivity.</text>')

    for y in tick_values(100, 450, 7):
        ry = scale_tiger(y)
        parts.append(f'<line x1="{margin_left}" y1="{ry}" x2="{width-margin_right}" y2="{ry}" stroke="#e8efe3" stroke-width="1"/>')
        parts.append(f'<text x="{margin_left-12}" y="{ry+4}" text-anchor="end" font-size="12" font-family="Arial" fill="#4b5563">{int(y)}</text>')

    for y in tick_values(39, 45, 6):
        ry = scale_forest(y)
        parts.append(f'<line x1="{margin_left}" y1="{ry}" x2="{width-margin_right}" y2="{ry}" stroke="#eef4ff" stroke-width="1" stroke-dasharray="4 4"/>')
        parts.append(f'<text x="{width-margin_right+12}" y="{ry+4}" text-anchor="start" font-size="12" font-family="Arial" fill="#4b5563">{y:.1f}</text>')

    parts.append(f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#183d2b" stroke-width="1.4"/>')
    parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#183d2b" stroke-width="1.4"/>')

    tiger_points = []
    for x, y in zip(x_values, y_values):
        px = scale_x(x)
        py = scale_tiger(y)
        tiger_points.append((px, py))
        parts.append(f'<circle cx="{px}" cy="{py}" r="6" fill="#2f6f4f" stroke="#ffffff" stroke-width="2"/>')
        parts.append(f'<text x="{px}" y="{height-margin_bottom+24}" text-anchor="middle" font-size="12" font-family="Arial" fill="#374151">{x}</text>')

    tiger_polyline = " ".join(f"{px},{py}" for px, py in tiger_points)
    tiger_area = tiger_polyline + f" {scale_x(x_values[-1])},{height-margin_bottom} {scale_x(x_values[0])},{height-margin_bottom}"
    parts.append(f'<polygon points="{tiger_area}" fill="#2f6f4f" fill-opacity="0.12"/>')
    parts.append(f'<polyline points="{tiger_polyline}" fill="none" stroke="#2f6f4f" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>')

    forest_points = []
    for x, y in zip(x_values, [39.6, 39.1, 44.74, 44.0, 40.36]):
        px = scale_x(x)
        py = scale_forest(y)
        forest_points.append((px, py))
        parts.append(f'<circle cx="{px}" cy="{py}" r="5" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>')

    forest_polyline = " ".join(f"{px},{py}" for px, py in forest_points)
    parts.append(f'<polyline points="{forest_polyline}" fill="none" stroke="#3b82f6" stroke-width="2.6" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"/>')

    parts.append('<rect x="520" y="96" width="128" height="58" rx="10" fill="#f8fbf7" stroke="#dce8d6"/>')
    parts.append('<circle cx="540" cy="118" r="5" fill="#2f6f4f"/>')
    parts.append('<circle cx="540" cy="142" r="5" fill="#3b82f6"/>')
    parts.append('<text x="552" y="122" font-size="12" font-family="Arial" fill="#374151">Tiger count</text>')
    parts.append('<text x="552" y="146" font-size="12" font-family="Arial" fill="#374151">Forest cover</text>')
    parts.append(f'<text x="{width/2}" y="{height-28}" text-anchor="middle" font-size="13" font-family="Arial" fill="#4b5563">Year</text>')
    parts.append(f'<text x="28" y="{height/2}" text-anchor="middle" transform="rotate(-90 28 {height/2})" font-size="13" font-family="Arial" fill="#4b5563">Count / cover</text>')
    parts.append('</svg>')
    path.write_text('\n'.join(parts), encoding='utf-8')


def svg_bar_chart(path, title, rows, x_key, y_key, color='#2f6f4f'):
    width = 760
    height = 460
    margin_left = 80
    margin_right = 40
    margin_top = 70
    margin_bottom = 100
    max_value = max(abs(row[y_key]) for row in rows)

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append('<rect x="0" y="0" width="100%" height="100%" fill="#fcfdf7"/>')
    parts.append('<rect x="20" y="20" width="720" height="420" rx="18" fill="#ffffff" stroke="#e0ebda" stroke-width="1.5"/>')
    parts.append(f'<text x="{width/2}" y="46" text-anchor="middle" font-size="20" font-family="Arial" fill="#183d2b" font-weight="700">{title}</text>')
    parts.append('<text x="80" y="62" font-size="12" font-family="Arial" fill="#4b5563">Positive gains in most parks, with Bardiya as the main exception.</text>')
    parts.append(f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#183d2b" stroke-width="1.4"/>')
    parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{height-margin_bottom}" stroke="#183d2b" stroke-width="1.4"/>')

    for tick in range(0, 6):
        y = margin_top + (height - margin_top - margin_bottom) * tick / 5
        parts.append(f'<line x1="{margin_left}" y1="{y}" x2="{width-margin_right}" y2="{y}" stroke="#eef3e9" stroke-width="1"/>')
        parts.append(f'<text x="{margin_left-12}" y="{y+4}" text-anchor="end" font-size="12" font-family="Arial" fill="#4b5563">{int(round(max_value - (max_value * tick / 5)))}</text>')

    for index, row in enumerate(rows):
        x = margin_left + index * 110 + 26
        y_base = height - margin_bottom
        bar_height = abs(row[y_key]) / max_value * 240
        bar_y = y_base - bar_height if row[y_key] >= 0 else y_base
        color_fill = color if row[y_key] >= 0 else '#dc2626'
        parts.append(f'<rect x="{x}" y="{bar_y}" width="70" height="{bar_height}" rx="8" fill="{color_fill}" fill-opacity="0.95"/>')
        parts.append(f'<line x1="{x+35}" y1="{y_base}" x2="{x+35}" y2="{y_base-8}" stroke="#94a3b8" stroke-width="1"/>')
        parts.append(f'<text x="{x+35}" y="{y_base+26}" text-anchor="middle" font-size="12" font-family="Arial" fill="#374151">{row[x_key]}</text>')
        parts.append(f'<text x="{x+35}" y="{bar_y-8}" text-anchor="middle" font-size="12" font-family="Arial" fill="{color_fill}">{row[y_key]}</text>')

    parts.append(f'<line x1="{margin_left}" y1="{height-margin_bottom}" x2="{width-margin_right}" y2="{height-margin_bottom}" stroke="#183d2b" stroke-width="1.4"/>')
    parts.append('</svg>')
    path.write_text('\n'.join(parts), encoding='utf-8')


def svg_habitat_map(path, title):
    width = 720
    height = 420
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append('<rect x="0" y="0" width="100%" height="100%" fill="#f6f8f2"/>')
    parts.append(f'<text x="{width/2}" y="28" text-anchor="middle" font-size="20" font-family="Arial" fill="#111">{title}</text>')
    parts.append('<path d="M120 140l56-44 70-10 68 16 54 8 40 34 8 46-20 46-54 22-44 8-48-12-40-36-10-42z" fill="#efe8d8" stroke="#2e3a2f" stroke-width="3"/>')
    parts.append('<path d="M156 184l42-20 38 8 18 28-16 24-38 10-28-14-16-26z" fill="#dfe9d8" stroke="#2e3a2f" stroke-width="2"/>')
    parts.append('<path d="M240 212l56-10 44 10 16 24-18 24-36 8-34-12-14-24z" fill="#e7efe2" stroke="#2e3a2f" stroke-width="2"/>')
    parts.append('<path d="M180 120c18-16 28-40 40-54" stroke="#5b8dc0" stroke-width="5" fill="none" stroke-linecap="round"/>')
    parts.append('<path d="M118 252c26 10 48 14 84 8" stroke="#5b8dc0" stroke-width="5" fill="none" stroke-linecap="round"/>')
    parts.append('<path d="M214 176l48 10 36 20 24 0" stroke="#2f6f4f" stroke-width="5" fill="none" stroke-linecap="round"/>')
    parts.append('<circle cx="212" cy="176" r="10" fill="#2f6f4f"/>')
    parts.append('<circle cx="260" cy="188" r="10" fill="#3b82f6"/>')
    parts.append('<circle cx="238" cy="248" r="10" fill="#7c3aed"/>')
    parts.append('<circle cx="320" cy="224" r="10" fill="#f59e0b"/>')
    parts.append('<circle cx="360" cy="200" r="10" fill="#dc2626"/>')
    parts.append('<text x="196" y="112" font-size="14" font-family="Arial" fill="#111">Nepal</text>')
    parts.append('<text x="132" y="320" font-size="14" font-family="Arial" fill="#111">Terai Arc Landscape • protected areas • corridors</text>')
    parts.append('</svg>')
    path.write_text('\n'.join(parts), encoding='utf-8')


if __name__ == '__main__':
    write_csv(DATA_DIR / 'tiger_data.csv', tiger_rows, ['year', 'tiger_count', 'method'])
    write_csv(DATA_DIR / 'forest_data.csv', forest_rows, ['year', 'forest_pct', 'source'])
    write_csv(DATA_DIR / 'park_change.csv', park_rows, ['park', 'change'])

    svg_line_chart(FIG_DIR / 'tiger_population.svg', "Nepal tiger population, 2000–2026", [2000, 2005, 2009, 2013, 2018, 2022, 2026], [109, 126, 121, 198, 235, 355, 429])
    svg_bar_chart(FIG_DIR / 'park_change.svg', 'Park-level tiger change, 2022–2026', park_rows, 'park', 'change')
    svg_habitat_map(FIG_DIR / 'habitat_map.svg', 'Terai habitat map')

    (BASE_DIR / 'README.md').write_text(
        'Analysis outputs\n================\n\n'
        'This folder contains exported data files and generated SVG figures for the updated Nepal tiger and forest-cover comparison.\n\n'
        'Files:\n'
        '- data/: CSV data tables\n'
        '- figures/: SVG figures for the web page and notebook export\n'
    )

    print('Export completed.')
    print('Files created:')
    for path in sorted([p for p in BASE_DIR.rglob('*') if p.is_file()]):
        print(path.relative_to(BASE_DIR))
