import nbformat as nbf

nb = nbf.v4.new_notebook()

md_header = """# Fase 4: Capas Complementarias (POI)
**Tema**: 2. Centralidad y corredores críticos de la red vial
**Requisito de Rúbrica**: Al menos una capa complementaria integrada espacialmente al grafo.

Para el análisis de corredores críticos, es clave entender **qué atrae el flujo vehicular**. Por ello, descargaremos Puntos de Interés (POI) que son grandes atractores de tráfico:
- Centros de salud (`amenity=hospital`, `clinic`)
- Centros educativos (`amenity=school`, `university`)
- Comercio mayor (`shop=mall`, `supermarket`)

Integraremos espacialmente estos POI identificando el nodo de la red vehicular más cercano a cada uno de ellos y asignando a dicho nodo el conteo de atractores."""

code_setup = """import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np

graphml_path = "../data/miraflores_drive_proj.graphml"
G_proj = ox.load_graphml(graphml_path)

print(f"Grafo cargado: {G_proj.number_of_nodes()} nodos, {G_proj.number_of_edges()} aristas.")"""

md_poi = """## Descarga de Atractores de Tráfico (POI)"""
code_poi = """place_name = "Miraflores, Provincia de Lima, Lima Metropolitana, Lima, Peru"
tags = {
    'amenity': ['hospital', 'clinic', 'school', 'university'],
    'shop': ['mall', 'supermarket']
}

print("Descargando POI desde OSM...")
gdf_poi = ox.features_from_place(place_name, tags=tags)
print(f"Se encontraron {len(gdf_poi)} POIs atractores de tráfico.")

# Limpiar geometría: Si hay polígonos, tomar su centroide
gdf_poi = gdf_poi.copy()
gdf_poi['geometry'] = gdf_poi.centroid

# Proyectar POIs al mismo CRS del grafo (EPSG:32718)
gdf_poi = gdf_poi.to_crs("EPSG:32718")"""

md_integrate = """## Integración Espacial
Buscaremos el nodo de la red vehicular más cercano a cada POI y contaremos cuántos POIs caen en el área de influencia de cada intersección."""

code_integrate = """# Obtener coordenadas X, Y
x = gdf_poi.geometry.x
y = gdf_poi.geometry.y

# Encontrar los nodos más cercanos a cada POI
print("Integrando POIs con la red vial...")
nearest_nodes = ox.distance.nearest_nodes(G_proj, X=x, Y=y)
gdf_poi['nearest_node'] = nearest_nodes

# Contar POIs por nodo
poi_counts = gdf_poi['nearest_node'].value_counts().to_dict()

# Asignar atributo al grafo
for n, data in G_proj.nodes(data=True):
    data['poi_count'] = str(poi_counts.get(n, 0))

nodos_con_poi = sum(1 for n, d in G_proj.nodes(data=True) if int(d['poi_count']) > 0)
print(f"Integración completa. {nodos_con_poi} nodos de la red son el acceso más cercano a uno o más POIs atractores.")"""

md_save = """## Guardar Grafo Enriquecido"""
code_save = """ox.save_graphml(G_proj, "../data/miraflores_drive_poi.graphml")
print("Grafo enriquecido con POIs guardado exitosamente.")"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_header),
    nbf.v4.new_code_cell(code_setup),
    nbf.v4.new_markdown_cell(md_poi),
    nbf.v4.new_code_cell(code_poi),
    nbf.v4.new_markdown_cell(md_integrate),
    nbf.v4.new_code_cell(code_integrate),
    nbf.v4.new_markdown_cell(md_save),
    nbf.v4.new_code_cell(code_save)
]

with open(r'C:\Users\jg153\Documents\202602\COMPLEX NETWORKS\TB1_COMPLEX\notebooks\03_capas_poi.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
