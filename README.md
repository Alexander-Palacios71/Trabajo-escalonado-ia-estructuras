# Selección y evaluación de registros sísmicos mediante Vertical Data Science

Este repositorio contiene el desarrollo de un proyecto de investigación orientado a la evaluación de registros sísmicos corregidos correspondientes a la **Zona Sísmica 3 del Perú**, utilizando técnicas de **Vertical Data Science** para su caracterización, análisis y selección con fines de aplicación en análisis no lineales tiempo-historia (Nonlinear Time History Analysis - NLTHA).

El objetivo principal es verificar que los registros acelerográficos cumplan con los criterios técnicos y normativos requeridos para su utilización en análisis dinámicos no lineales. Para ello, se analizarán sus características sísmicas y su compatibilidad espectral, permitiendo identificar aquellos registros que representen adecuadamente la amenaza sísmica de la zona de estudio.

Una vez seleccionados los registros, estos serán aplicados al análisis no lineal tiempo-historia de una estructura, con el propósito de evaluar su respuesta sísmica mediante indicadores como derivas de entrepiso, desplazamientos y nivel de desempeño estructural de acuerdo con normas internacionales.

El proyecto integra herramientas de Ciencia de Datos e Ingeniería Sísmica para desarrollar una metodología reproducible que facilite la selección de acelerogramas y contribuya a mejorar la confiabilidad de las evaluaciones estructurales.

## Fuente de datos

Los registros acelerográficos utilizados en este proyecto serán obtenidos del **Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID)** mediante la Red Acelerográfica del CISMID (REDACIS):

https://www.cismid.uni.edu.pe/ceois/redacis/red/

En caso de ser necesario, la información podrá complementarse con registros oficiales publicados por el Instituto Geofísico del Perú (IGP).

## Estado del proyecto

Actualmente el proyecto se encuentra en fase de desarrollo e incluye las siguientes actividades:

- Recolección de registros sísmicos.
- Caracterización y análisis mediante Vertical Data Science.
- Evaluación de compatibilidad espectral.
- Selección de registros para análisis no lineal tiempo-historia.
- Evaluación del desempeño estructural.

## Tecnologías

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Scikit-learn
- Jupyter Notebook
- ETABS / OpenSees (Análisis estructural)
