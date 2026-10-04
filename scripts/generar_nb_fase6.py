import nbformat as nbf

nb = nbf.v4.new_notebook()

md_header = """# Fase 6: Métricas Específicas - Centralidad y Corredores Críticos
**Tema**: 2. Centralidad y corredores críticos de la red vial
**Requisito de Rúbrica**: Métrica dependiente del tema con parámetros justificados.

Calcularemos las métricas de centralidad que permitirán identificar los corredores críticos:
1. **Betweenness Centrality (Intermediación)**
2. **Closeness Centrality (Cercanía)**

**Justificación del Rigor Algorítmico**: El cálculo exacto tiene complejidad $O(NM)$. Dado que nuestro grafo tiene $N \\approx 2500$ nodos, calcularemos la medida exacta utilizando la longitud (`length`), evitando la aproximación por muestreo ($k$)."""

code_setup = """import osmnx as ox
import networkx as nx
import pandas as pd
import time

G = ox.load_graphml("../data/miraflores_drive_poi.graphml")
print(f"Grafo cargado: {G.number_of_nodes()} nodos, {G.number_of_edges()} aristas.")"""

md_betweenness = """## Betweenness Centrality (Intermediación)"""
code_betweenness = """print("Calculando Betweenness Centrality exacto...")
start_time = time.time()
bc = nx.betweenness_centrality(G, weight='length', normalized=True)
nx.set_node_attributes(G, bc, 'betweenness')
print(f"Completado en {time.time() - start_time:.2f} segundos.")"""

md_closeness = """## Closeness Centrality (Cercanía)"""
code_closeness = """print("Calculando Closeness Centrality exacto...")
start_time = time.time()
cc = nx.closeness_centrality(G, distance='length')
nx.set_node_attributes(G, cc, 'closeness')
print(f"Completado en {time.time() - start_time:.2f} segundos.")"""

md_corridors = """## Identificación de Corredores Críticos"""
code_corridors = """nodes, edges = ox.graph_to_gdfs(G)
threshold = nodes['betweenness'].quantile(0.95)
print(f"Umbral de Betweenness (Top 5%): {threshold:.4f}")

critical_nodes = {n: (1 if bc_val >= threshold else 0) for n, bc_val in bc.items()}
nx.set_node_attributes(G, critical_nodes, 'is_critical')

n_critical = sum(critical_nodes.values())
print(f"Se identificaron {n_critical} nodos críticos.")"""

md_save = """## Guardar Grafo Analizado"""
code_save = """out_path = "../data/miraflores_drive_centralities.graphml"
ox.save_graphml(G, out_path)
print(f"Grafo guardado en {out_path}")"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(md_header),
    nbf.v4.new_code_cell(code_setup),
    nbf.v4.new_markdown_cell(md_betweenness),
    nbf.v4.new_code_cell(code_betweenness),
    nbf.v4.new_markdown_cell(md_closeness),
    nbf.v4.new_code_cell(code_closeness),
    nbf.v4.new_markdown_cell(md_corridors),
    nbf.v4.new_code_cell(code_corridors),
    nbf.v4.new_markdown_cell(md_save),
    nbf.v4.new_code_cell(code_save)
]

with open(r'C:\Users\jg153\Documents\202602\COMPLEX NETWORKS\TB1_COMPLEX\notebooks\05_centralidades_corredores.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
