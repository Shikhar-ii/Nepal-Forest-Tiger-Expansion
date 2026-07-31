from pathlib import Path
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import geopandas as gpd
import osmnx as ox
import contextily as ctx
from shapely.geometry import Polygon, Point

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

park_locations = [
    {'park': 'Chitwan', 'lat': 27.5345, 'lon': 84.3574},
    {'park': 'Parsa', 'lat': 27.1365, 'lon': 84.2596},
    {'park': 'Banke', 'lat': 28.0274, 'lon': 81.7138},
    {'park': 'Bardiya', 'lat': 28.8265, 'lon': 81.4200},
    {'park': 'Shuklaphanta', 'lat': 28.6767, 'lon': 80.1231},
]

TERAI_POLYGON = [
    (80.0, 26.5),
    (87.7, 26.5),
    (87.7, 28.8),
    (80.0, 28.8),
    (80.0, 26.5),
]


def write_csv(path, rows, fieldnames):
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def save_tiger_forest_timeline():
    df_tiger = pd.DataFrame(tiger_rows)
    df_forest = pd.DataFrame(forest_rows)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_tiger['year'], df_tiger['tiger_count'], marker='o', color='#1f7765', linewidth=3, label='Tiger count')
    ax.set_ylabel('Tiger count', color='#1f7765', fontsize=12)
    ax.set_ylim(90, 460)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_xticks(sorted(set(df_tiger['year'].tolist() + df_forest['year'].tolist())))
    ax.tick_params(axis='y', colors='#1f7765')
    ax.spines['left'].set_color('#1f7765')

    ax2 = ax.twinx()
    ax2.plot(df_forest['year'], df_forest['forest_pct'], marker='o', linestyle='--', color='#1d4ed8', linewidth=2.5, label='Forest cover')
    ax2.set_ylabel('Forest cover (%)', color='#1d4ed8', fontsize=12)
    ax2.set_ylim(38, 46)
    ax2.tick_params(axis='y', colors='#1d4ed8')
    ax2.spines['right'].set_color('#1d4ed8')

    fig.suptitle('Nepal tiger population and forest cover, 2000–2026', fontsize=18, fontweight='700')
    ax.grid(axis='y', color='#d8e7df', linestyle='-', linewidth=0.9, alpha=0.65)
    ax2.grid(False)
    ax.set_facecolor('#fbfcfb')
    fig.patch.set_facecolor('#fbfcfb')

    ax.legend(loc='upper left', frameon=False)
    ax2.legend(loc='upper right', frameon=False)

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(FIG_DIR / 'tiger_forest_timeline.svg', format='svg', dpi=200)
    plt.close(fig)


def save_park_change_chart():
    df = pd.DataFrame(park_rows)
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ['#1f7765' if x >= 0 else '#dc2626' for x in df['change']]
    ax.bar(df['park'], df['change'], color=colors, edgecolor='none', width=0.58)
    ax.axhline(0, color='#111827', linewidth=1.2)
    ax.set_ylabel('Tiger change', fontsize=12)
    ax.set_title('Park-level tiger change, 2022–2026', fontsize=18, fontweight='700')
    ax.set_facecolor('#fbfcfb')
    ax.grid(axis='y', color='#e6eef0', linestyle='-', linewidth=0.9)
    ax.set_axisbelow(True)
    ax.set_xlabel('Protected area', fontsize=12)
    ax.set_ylim(min(df['change']) - 8, max(df['change']) + 8)
    for idx, row in df.iterrows():
        ax.text(idx, row['change'] + (2 if row['change'] >= 0 else -4), f"{row['change']}", ha='center', va='bottom' if row['change'] >= 0 else 'top', color=colors[idx], fontsize=11, fontweight='600')

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'park_change.svg', format='svg', dpi=200)
    plt.close(fig)


def save_habitat_map():
    nepal = ox.geocode_to_gdf('Nepal')
    nepal = nepal.to_crs(epsg=3857)
    terai = Polygon(TERAI_POLYGON)
    terai_gdf = gpd.GeoDataFrame({'name': ['Terai Arc Landscape']}, geometry=[terai], crs='EPSG:4326').to_crs(epsg=3857)
    parks = gpd.GeoDataFrame(park_locations, geometry=[Point(r['lon'], r['lat']) for r in park_locations], crs='EPSG:4326').to_crs(epsg=3857)

    fig, ax = plt.subplots(figsize=(12, 10))
    nepal.plot(ax=ax, color='#f6f2e8', edgecolor='#525252', linewidth=1.4)
    terai_gdf.plot(ax=ax, color='#60a5fa', alpha=0.24, edgecolor='#2563eb', linewidth=2)
    parks.plot(ax=ax, color='#dc2626', edgecolor='#ffffff', linewidth=1.4, markersize=150)

    for _, row in parks.iterrows():
        ax.text(row.geometry.x + 15000, row.geometry.y + 12000, row['park'], fontsize=11, fontweight='600', color='#111827', bbox=dict(facecolor='white', edgecolor='none', alpha=0.72, boxstyle='round,pad=0.2'))

    ax.set_axis_off()
    bounds = terai_gdf.total_bounds
    margin = 150000
    ax.set_xlim(bounds[0] - margin, bounds[2] + margin)
    ax.set_ylim(bounds[1] - margin, bounds[3] + margin)
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik, crs=nepal.crs)

    ax.set_title('OpenStreetMap-based Terai habitat and tiger park overview', fontsize=18, fontweight='700', pad=18)
    fig.patch.set_facecolor('#fbfcfb')

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'habitat_map.png', dpi=200, bbox_inches='tight', pad_inches=0.08)
    fig.savefig(FIG_DIR / 'habitat_map.svg', format='svg', dpi=200, bbox_inches='tight', pad_inches=0.08)
    plt.close(fig)


if __name__ == '__main__':
    write_csv(DATA_DIR / 'tiger_data.csv', tiger_rows, ['year', 'tiger_count', 'method'])
    write_csv(DATA_DIR / 'forest_data.csv', forest_rows, ['year', 'forest_pct', 'source'])
    write_csv(DATA_DIR / 'park_change.csv', park_rows, ['park', 'change'])

    save_tiger_forest_timeline()
    save_park_change_chart()
    save_habitat_map()

    (BASE_DIR / 'README.md').write_text(
        'Analysis outputs\n================\n\n'
        'This folder contains exported data files and generated figures for the updated Nepal tiger and forest cover project.\n\n'
        'Files:\n'
        '- data/: CSV data tables\n'
        '- figures/: charts and OpenStreetMap-based habitat visuals generated by Python\n',
        encoding='utf-8'
    )

    print('Export completed.')
    print('Files created:')
    for path in sorted([p for p in FIG_DIR.rglob('*') if p.is_file()]):
        print(path.name)
