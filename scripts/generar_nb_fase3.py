import nbformat as nbf

nb = nbf.v4.new_notebook()

md_header = """# Fase 3: Limpieza y Proyección Espacial
**Tema**: 2. Centralidad y corredores críticos de la red vial
**Requisito de Rúbrica**: 
- Proyección a EPSG:32718 (CRS métrico local para Lima) antes de cualquier cálculo espacial.
- Reportar % de aristas con datos faltantes en `maxspeed`, `lanes`, `name` y explicar su tratamiento.
- Documentar el uso de `simplify=True` (aplicado en Fase 2)."""

code_setup = """import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np

# Cargar el grafo no proyectado
graphml_path = "../data/miraflores_drive.graphml"
G = ox.load_graphml(graphml_path)

print(f"Nodos iniciales: {G.number_of_nodes()}")
print(f"Aristas iniciales: {G.number_of_edges()}")"""

md_proj = """## Proyección Espacial (EPSG:32718)"""
code_proj = """G_proj = ox.project_graph(G, to_crs="EPSG:32718")
print(f"CRS del grafo proyectado: {G_proj.graph['crs']}")"""

md_missing = """## Análisis y Tratamiento de Valores Faltantes"""
code_missing = """_, edges = ox.graph_to_gdfs(G_proj)

def is_missing(val):
    if isinstance(val, list): return False
    return pd.isna(val)

missing_maxspeed = edges['maxspeed'].apply(is_missing).mean() if 'maxspeed' in edges.columns else 1.0
missing_lanes = edges['lanes'].apply(is_missing).mean() if 'lanes' in edges.columns else 1.0
missing_name = edges['name'].apply(is_missing).mean() if 'name' in edges.columns else 1.0

print(f"% faltantes en maxspeed: {missing_maxspeed*100:.2f}%")
print(f"% faltantes en lanes: {missing_lanes*100:.2f}%")
print(f"% faltantes en name: {missing_name*100:.2f}%")

hwy_speeds = {'primary': 50, 'secondary': 40, 'tertiary': 30, 'residential': 20, 'unclassified': 30}

for u, v, k, data in G_proj.edges(keys=True, data=True):
    hw = data.get('highway', 'unclassified')
    if isinstance(hw, list): hw = hw[0]
    
    if is_missing(data.get('maxspeed')):
        data['maxspeed'] = str(hwy_speeds.get(hw, 30))
    if is_missing(data.get('lanes')):
        data['lanes'] = '1'
    if is_missing(data.get('name')):
        data['name'] = 'Sin nombre'
        
print("Tratamiento de valores nulos completado y escrito en el grafo.")"""

md_save = """## Guardar Grafo Proyectado y Limpio"""
code_save = """ox.save_graphml(G_proj, "../data/miraflores_drive_proj.graphml")
print("Grafo proyectado guardado.")"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_header),
    nbf.v4.new_code_cell(code_setup),
    nbf.v4.new_markdown_cell(md_proj),
    nbf.v4.new_code_cell(code_proj),
    nbf.v4.new_markdown_cell(md_missing),
    nbf.v4.new_code_cell(code_missing),
    nbf.v4.new_markdown_cell(md_save),
    nbf.v4.new_code_cell(code_save)
]

with open(r'C:\Users\jg153\Documents\202602\COMPLEX NETWORKS\TB1_COMPLEX\notebooks\02_limpieza_y_proyeccion.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
