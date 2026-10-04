# Course Knowledge Base - Complex Networks 2026-02

## Conceptos Cubiertos
- **Teoría de Redes Básica**: Grafos dirigidos, no dirigidos y ponderados. Grado, densidad, conectividad, componentes conexas, caminos más cortos, diámetro, clustering coefficient (local y global).
- **Modelos de Redes**:
  - *Redes Aleatorias* (Erdős–Rényi): Distribución de Poisson/binomial, diámetro O(log N), bajo clustering.
  - *Redes de Pequeño Mundo* (Watts-Strogatz): Efecto de atajos (rewiring probability $p$), alto clustering, distancia promedio baja.
  - *Redes Scale-Free* (Barabási–Albert): Preferential attachment, hubs, distribución de grado de ley de potencias.
- **Centralidades**:
  - *Basadas en grado/conectividad*: Degree Centrality, Eigenvector Centrality, PageRank, Katz Centrality.
  - *Geométricas (Caminos Cortos)*: Closeness Centrality, Harmonic Centrality, Betweenness Centrality.
- **Asortatividad y Mezcla Selectiva (Assortative Mixing)**: Homofilia, asortatividad de grado y de atributos (Newman), KNNK, Multiscale Mixing, Conformity.
- **Detección de Comunidades**: Louvain (optimización de modularidad), Girvan-Newman (remoción por betweenness), Propagación de Etiquetas, Infomap, cliques.

## Convenciones de Notación de Clase
- **Representación de Grafos**: $N$ para número de nodos, $L$ o $m$ para número de enlaces.
- **Probabilidades y Grados**: $p$ para probabilidad de conexión/rewiring, $k$ para grado de un nodo, $<k>$ para grado promedio, $P(k)$ para distribución de grado.
- **Métricas**: $C$ para coeficiente de clustering, $d$ para distancia o caminos más cortos, $r$ para asortatividad.
- **Estilo de Análisis**: Preferencia por normalización y justificación de métricas según el fenómeno a estudiar (p. ej., si la información no fluye por caminos más cortos, no usar betweenness). 

## Ejemplos y Plantillas de Código (Estilo a seguir)
El profesor (Andrés Gibu) utiliza `networkx` junto a `matplotlib` (y a veces `seaborn`, `pandas`, `powerlaw` o librerías específicas como `MultiscaleMixing`, `node_conformity`).
El código típico usa `nx.Graph()` / `nx.DiGraph()`, seguido de cálculo de métricas usando diccionarios, y visualizaciones con `nx.draw()` pasándole paletas de colores basadas en métricas.

**Ejemplo de cálculo y visualización de centralidad (Patrón de clase):**
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
pos = nx.spring_layout(G)

# Cálculo
pagerank = nx.pagerank(G)
formateed_pagerank = {node: f'{rank:.2f}' for node, rank in pagerank.items()}
print("PageRank:" , formateed_pagerank)

# Visualización usando los valores calculados como colores
nx.draw(G, pos, with_labels=True, node_color=list(pagerank.values()), cmap=plt.cm.Reds)
plt.show()
```

**Ejemplo de modelo nulo (Distribución de grado de Red Aleatoria):**
```python
G_er = nx.erdos_renyi_graph(n=100, p=0.05)
degrees = [deg for node, deg in G_er.degree()]
sns.histplot(degrees, bins=range(min(degrees), max(degrees)+1), kde=False)
plt.title("Distribución de Grados")
plt.xlabel("Grado")
plt.ylabel("Frecuencia")
plt.show()
```

El código de los proyectos deberá mantener este estilo: directo, fuertemente apoyado en `networkx`, utilizando diccionarios por comprensión para iterar sobre métricas y `matplotlib` para la generación de gráficas (o `osmnx` y `geopandas` para los análisis espaciales, como lo requiere el hito).
