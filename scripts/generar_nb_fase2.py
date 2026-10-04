import nbformat as nbf
import datetime
import os

nb = nbf.v4.new_notebook()

# Markdown cell: Header
md_header = """# Fase 2: Descarga de la Red Vial de Miraflores
**Tema**: 2. Centralidad y corredores críticos de la red vial
**Área de estudio**: Distrito de Miraflores, Lima Metropolitana, Perú
**Tipo de red (network_type)**: `drive` (vehicular). Justificación: El análisis de corredores críticos y congestión estructural en el territorio impacta principalmente al flujo vehicular, cuyas rutas de menor costo son dictadas por el trazado de las avenidas principales y el sentido de las vías (`oneway`).

## Configuración y Reproducibilidad"""

# Code cell: Imports and seed
code_setup = """import osmnx as ox
import networkx as nx
import datetime
import random
import numpy as np

# Fijar semilla de reproducibilidad
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# Versiones de librerías
print(f"OSMnx version: {ox.__version__}")
print(f"NetworkX version: {nx.__version__}")
print(f"Fecha de ejecución: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")"""

# Markdown cell: Download
md_download = """## Descarga del Grafo
Utilizamos la API de Overpass a través de OSMnx para obtener el grafo espacial.
Solicitamos explícitamente `simplify=True` para reducir nodos intermedios de geometría plana, tal como exige la rúbrica."""

# Code cell: Download
code_download = """place_name = "Miraflores, Provincia de Lima, Lima Metropolitana, Lima, Peru"
network_type = "drive"

print(f"Descargando grafo para: {place_name}")
print('Query implícita a Overpass: area["name"="Miraflores"]... way["highway"]...')

# Descarga del grafo
G = ox.graph_from_place(place_name, network_type=network_type, simplify=True)

print(f"Número de nodos: {G.number_of_nodes()}")
print(f"Número de aristas: {G.number_of_edges()}")"""

# Markdown cell: Saving
md_save = """## Guardado de Datos Intermedios
Exportamos el grafo a formato GraphML y GeoPackage para asegurar reproducibilidad sin depender de futuras consultas a la API."""

# Code cell: Saving
code_save = """import os
os.makedirs("../data", exist_ok=True)

# Guardar en GraphML
graphml_path = "../data/miraflores_drive.graphml"
ox.save_graphml(G, graphml_path)
print(f"Grafo guardado en {graphml_path}")

# Guardar en GeoPackage (requiere convertir el grafo a GeoDataFrames)
gpkg_path = "../data/miraflores_drive.gpkg"
gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)
gdf_nodes.to_file(gpkg_path, layer='nodes', driver="GPKG")
gdf_edges.to_file(gpkg_path, layer='edges', driver="GPKG")
print(f"Grafo guardado en {gpkg_path} (Capa 'nodes' y 'edges')")"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_header),
    nbf.v4.new_code_cell(code_setup),
    nbf.v4.new_markdown_cell(md_download),
    nbf.v4.new_code_cell(code_download),
    nbf.v4.new_markdown_cell(md_save),
    nbf.v4.new_code_cell(code_save)
]

notebook_path = r"C:\Users\jg153\Documents\202602\COMPLEX NETWORKS\TB1_COMPLEX\notebooks\01_descarga_osm.ipynb"
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Notebook creado en {notebook_path}")
