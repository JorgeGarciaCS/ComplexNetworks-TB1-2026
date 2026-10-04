import nbformat as nbf

nb = nbf.v4.new_notebook()

md_header = """# Fase 5: EDA Espacial y Métricas Globales
**Tema**: 2. Centralidad y corredores críticos de la red vial

En esta fase calcularemos las métricas globales del grafo. Como indica la rúbrica, todas las métricas dependientes de la escala (como la longitud total o las intersecciones) deben estar normalizadas por el área del distrito para permitir comparaciones justas."""

code_setup = """import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np

# Cargar el grafo enriquecido y proyectado
G = ox.load_graphml("../data/miraflores_drive_poi.graphml")

# Obtener los GeoDataFrames
nodes, edges = ox.graph_to_gdfs(G)"""

md_area = """## Cálculo de Área y Normalización"""

code_area = """# Descargar el polígono de Miraflores para calcular el área exacta
distrito = ox.geocode_to_gdf("Miraflores, Provincia de Lima, Lima Metropolitana, Lima, Peru")
distrito_proj = distrito.to_crs(G.graph['crs'])

area_m2 = distrito_proj.geometry.area.iloc[0]
area_km2 = area_m2 / 1e6
print(f"Área del distrito de Miraflores: {area_km2:.2f} km²")"""

md_metrics = """## Métricas Globales (OSMnx y NetworkX)"""

code_metrics = """# 1. Nodos, aristas y grado medio
n_nodes = G.number_of_nodes()
n_edges = G.number_of_edges()

avg_degree = sum(dict(G.degree()).values()) / float(n_nodes)

# 2. Longitud total
total_length_m = edges['length'].astype(float).sum()
total_length_km = total_length_m / 1000
length_density = total_length_km / area_km2

# 3. Densidad de intersecciones
intersections = sum(1 for n, d in G.degree() if d > 2)
intersection_density = intersections / area_km2

print("=== MÉTRICAS GLOBALES ESPACIALES ===")
print(f"Nodos: {n_nodes}")
print(f"Aristas: {n_edges}")
print(f"Grado medio (degree): {avg_degree:.2f}")
print(f"Longitud total de red: {total_length_km:.2f} km")
print(f"Densidad de red (km/km²): {length_density:.2f}")
print(f"Intersecciones: {intersections}")
print(f"Densidad de intersecciones (por km²): {intersection_density:.2f}")"""

md_components = """## Conectividad y Diámetro"""

code_components = """# Número de componentes fuertemente conectados (SCC)
scc = list(nx.strongly_connected_components(G))
print(f"Número de SCCs: {len(scc)}")

# Extraer el Giant Component (la red principal conectada)
G_giant = G.subgraph(max(scc, key=len)).copy()
print(f"Nodos en el Giant Component: {G_giant.number_of_nodes()} ({(G_giant.number_of_nodes()/n_nodes)*100:.1f}% de la red)")

try:
    print("Calculando diámetro del Giant Component... (puede demorar)")
    # En grafos no ponderados, nx.diameter usa shortest_path
    diameter = nx.diameter(G_giant)
    print(f"Diámetro topológico (número de aristas): {diameter}")
except Exception as e:
    print("Error al calcular el diámetro exacto:", e)

# Edge Circuity (usando basic_stats de OSMnx)
try:
    stats = ox.basic_stats(G, area=area_m2)
    circuity = stats.get('circuity_avg', 'No disponible en esta versión')
    print(f"Circuity promedio de la red: {circuity}")
except Exception as e:
    print(f"Circuity promedio de la red: No disponible ({e})")"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_header),
    nbf.v4.new_code_cell(code_setup),
    nbf.v4.new_markdown_cell(md_area),
    nbf.v4.new_code_cell(code_area),
    nbf.v4.new_markdown_cell(md_metrics),
    nbf.v4.new_code_cell(code_metrics),
    nbf.v4.new_markdown_cell(md_components),
    nbf.v4.new_code_cell(code_components)
]

with open(r'C:\Users\jg153\Documents\202602\COMPLEX NETWORKS\TB1_COMPLEX\notebooks\04_eda_metricas_globales.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
