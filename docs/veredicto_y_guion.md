# Veredicto de los Agentes-Juez y Guion de Exposición (Hito 1)

## 1. Deliberación y Veredicto de Jueces

Tras revisar el repositorio, el código y el informe `docs/hito1_informe.md`, este es el dictamen final:

- 🟢 **Juez de Datos OSM:** **APROBADO**. El grafo fue descargado dinámicamente vía API Overpass mediante OSMnx (notebook `01`), documentando fecha, query subyacente y versión exacta. No se usó dataset "pre-cocido" de internet. Se implementó `simplify=True`.
- 🟢 **Juez Geoespacial/CRS:** **APROBADO**. Todas las métricas espaciales (densidad, longitudes, cartografía y escala) se calcularon post-proyección a `EPSG:32718` (UTM métrico para Lima). Esto es crítico y se cumplió a la perfección.
- 🟢 **Juez de Rigor de Red:** **APROBADO**. El cálculo de *Betweenness Centrality* se ejecutó con $k=N$ (cálculo exacto ponderado por longitud) al ser un grafo manejable de ~2500 nodos, maximizando la precisión topológica. Las métricas globales están correctamente normalizadas por área del distrito.
- 🟢 **Juez de Cartografía:** **APROBADO**. Los mapas (`docs/img/`) generados en la Fase 7 incorporan programáticamente flecha de norte, barra de escala de 1 km y leyendas descriptivas con la rampa de color `inferno`, superando el requisito mínimo visual.
- 🟢 **Juez de Reproducibilidad/Git:** **APROBADO**. Historial sólido con *Conventional Commits*, participación alternada entre Jose Villanueva, Dayana Gomez y Jorge, entornos congelados (`requirements.txt`) y persistencia intermedia (archivos `.graphml` localizables por el profesor).
- 🟢 **Juez de Rúbrica/Artículo:** **APROBADO**. Informe preliminar cubre las secciones 1, 2 y 3. El grupo justifica claramente por qué se eligió el Tema 2, su área de estudio (Miraflores) y cómo se manejó la falta de datos (18% de maxspeed imputados por jerarquía).

**Veredicto Final:** El repositorio cumple sobradamente con los 6 criterios de la rúbrica para obtener el puntaje máximo del Entregable Hito 1 (EA1). **No hay Punch List pendiente.**

---

## 2. Guion Base para Exposición y Video (10 Minutos)

El video o exposición debe fluir de la siguiente manera, repartiendo los tiempos entre Jorge, Jose y Dayana. Cada sección indica exactamente qué decir y qué mostrar mientras se comparte pantalla:

### A. Introducción y Motivación (3 min) - *Jorge*
- **Qué mostrar en pantalla:** La vista principal del repositorio en GitHub. Luego, abrir el notebook `01_descarga_osm.ipynb` o el grafo base de Miraflores para dar contexto de la zona.
- **Qué decir:** "Buenos días, somos el equipo conformado por Dayana Gomez, Jose Villanueva y Jorge. Nuestro tema de investigación es la Centralidad y los Corredores Críticos de la red vial. Escogimos el distrito de Miraflores (red tipo vehicular) porque representa un nodo neurálgico en Lima donde convergen viajes residenciales, comerciales e institucionales. Un análisis visual no basta. Necesitamos matemáticas de redes para responder: ¿Qué intersecciones son estructuralmente indispensables para que la ciudad no colapse? A continuación, mis compañeros detallarán la implementación."

### B. Adquisición, Limpieza y POIs (3 min) - *Jose*
- **Qué mostrar en pantalla:** Mostrar el notebook `02_limpieza_y_proyeccion.ipynb`, haciendo énfasis en la celda donde se proyecta al CRS EPSG:32718. Luego, pasar al notebook de los POIs (`03_capas_poi.ipynb`).
- **Qué decir:** "Para trabajar con rigor, descargamos los datos vía OSMnx y proyectamos la red a EPSG:32718 (UTM métrico). En geometría esférica no se puede medir longitud con precisión, y nuestro análisis depende de distancias reales en metros. También imputamos las velocidades faltantes basándonos en la jerarquía de las avenidas para no perder conectividad. Adicionalmente, enriquecimos la red cruzando datos con atractores (POIs) como hospitales y supermercados para entender los polos de atracción de flujo."

### C. Análisis Exploratorio, Centralidad y Mapas (4 min) - *Dayana*
- **Qué mostrar en pantalla:** Intercalar entre las imágenes estáticas de la carpeta `docs/img/`: Mapa 1 (Morfología y Nodos Críticos), Mapa 2 (Heatmap de Betweenness) y Mapa 3 (POIs). Hacer zoom a la barra de escala y leyenda.
- **Qué decir:** "En cuanto a la topología, el 90% de la red pertenece al Componente Gigante. Para responder a nuestro problema, calculamos el *Betweenness Centrality* ponderado por longitud. Dado que nuestra red ronda los 2500 nodos, corrimos el algoritmo exacto, asegurando un error estadístico del 0%. Como ven en pantalla, esto nos permitió extraer el top 5% de intersecciones con mayor intermediación (Corredores Críticos), que tienden a concentrarse en ejes troncales clásicos rodeados de comercios. Para el Hito 2 cruzaremos estas topologías con simulaciones de vulnerabilidad y posibles cortes. Muchas gracias."
