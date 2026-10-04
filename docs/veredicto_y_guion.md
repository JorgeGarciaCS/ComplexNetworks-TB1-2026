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

El video o exposición debe fluir de la siguiente manera, repartiendo los tiempos entre Dayana, Jose y Jorge:

### A. Introducción y Motivación (2 min) - *Jorge*
- **Apertura:** "Buenos días, somos el equipo conformado por Dayana Gomez, Jose Villanueva y Jorge. Nuestro tema de investigación es la Centralidad y los Corredores Críticos de la red vial."
- **Caso de Estudio:** "Escogimos el distrito de Miraflores (red tipo vehicular) porque representa un nodo neurálgico en Lima donde convergen viajes residenciales, comerciales e institucionales."
- **El Problema:** "Un análisis visual no basta. Necesitamos matemáticas de redes para responder: ¿Qué intersecciones son estructuralmente indispensables para que la ciudad no colapse?"

### B. Adquisición y Rigor Espacial (2 min) - *Jose*
- **Descarga:** "Utilizamos OSMnx para descargar los datos directamente de la API, documentando la semilla y fecha para reproducibilidad."
- **Limpieza y Proyección:** "Un paso vital: proyectamos la red a EPSG:32718. En geometría esférica no se puede medir longitud con precisión, y nuestro análisis depende de distancias en metros. También imputamos las velocidades faltantes (un 18%) basándonos en la jerarquía de las avenidas para no perder conectividad."
- **Capas extra:** "Para enriquecer el análisis, hicimos un cruce espacial identificando el nodo más cercano a atractores como hospitales, supermercados y colegios (POIs), lo que nos permite entender hacia dónde se dirige el flujo."

### C. Análisis Exploratorio y Métricas (2 min) - *Dayana*
- "Analizamos las métricas básicas, y, como dicta la buena práctica, las normalizamos por el área del polígono del distrito (9.62 km²)."
- "Tenemos una densidad de ~52 kilómetros de vía y 200 intersecciones reales por cada km². Además, descubrimos que más del 90% del grafo vehicular pertenece al Componente Gigante, probando que la red está altamente conectada, aunque sujeta a cuellos de botella."

### D. Métricas Específicas del Tema 2 (2 min) - *Jose*
- "Entrando a nuestra métrica central: Calculamos el *Betweenness Centrality* ponderado por longitud. Dado que nuestra red ronda los 2500 nodos, decidimos correr el algoritmo exacto en lugar de aproximarlo por muestreo, asegurando un error estadístico del 0%."
- "El resultado nos permitió extraer de forma analítica el top 5% de intersecciones con mayor intermediación, a los que etiquetamos como Corredores Críticos, ya que por ahí pasan estadísticamente más rutas eficientes."

### E. Cartografía y Conclusiones (2 min) - *Dayana y Jose*
- **Dayana:** "Visualmente, lo plasmamos en tres mapas cartográficamente rigurosos, con su respectiva escala métrica y orientación al norte. Vemos en el mapa de calor que el Betweenness tiende a concentrarse en ejes troncales clásicos de Miraflores, rodeados de atractores comerciales y de salud."
- **Jose:** "Concluyendo el Hito 1: Tenemos un pipeline 100% automatizado, reproducible y espacialmente correcto. La infraestructura está lista. Para el Hito 2 (artículo final), cruzaremos estas topologías con simulaciones de vulnerabilidad y posibles ataques a los nodos para comprobar qué tanto resiste este distrito a los cierres vehiculares. Muchas gracias."
