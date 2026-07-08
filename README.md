# TF1: Propuesta de Datos - Aplicaciones de IA en Estructuras

## Título de investigación
Selección y evaluación de registros sísmicos corregidos mediante Vertical Data Science
para análisis no lineales tiempo-historia de estructuras ubicadas en la Zona Sísmica 3 del Perú.

## Integrantes
- Palacios Rojas Alexander Ítalo
- Cristobal Villanueva Jhon Franklin
- Quintana Huayta Gisela Shenna
- Segura Sanchez José Gustavo

## Docente
Kurt Walter Soncco Sinchi — Julio, 2026

# Descripción

Este proyecto desarrolla una metodología basada en **Vertical Data Science (VDS)** para la caracterización, evaluación y selección de registros sísmicos corregidos correspondientes a la **Zona Sísmica 3 del Perú**, con el objetivo de verificar su aptitud para ser utilizados en **Análisis No Lineal Tiempo-Historia (Nonlinear Time History Analysis - NLTHA)**.

Posteriormente, los registros seleccionados serán aplicados al análisis dinámico no lineal de una estructura para evaluar su desempeño sísmico mediante indicadores como:

- Derivas máximas de entrepiso.
- Desplazamientos máximos.
- Cortante basal.
- Nivel de desempeño estructural.
- Estado de daño.

La investigación integra herramientas de Ciencia de Datos con criterios de Ingeniería Sísmica establecidos en normas internacionales como **ASCE 7**, **ASCE 41** y recomendaciones del **PEER Ground Motion Selection**.

---

# Objetivo General

Evaluar registros sísmicos corregidos mediante técnicas de Vertical Data Science para verificar su aptitud en análisis no lineales tiempo-historia y analizar el desempeño sísmico de una estructura de acuerdo con criterios normativos internacionales.

---

# Objetivos Específicos

- Caracterizar registros sísmicos corregidos mediante técnicas de Vertical Data Science.
- Analizar las propiedades dinámicas de cada acelerograma.
- Verificar la compatibilidad espectral de los registros conforme a criterios normativos.
- Seleccionar registros adecuados para análisis no lineal tiempo-historia.
- Evaluar la respuesta estructural utilizando los registros seleccionados.
- Analizar el desempeño sísmico de la estructura mediante indicadores de daño.

---

# Flujo de la investigación

```text
                 Registros Sísmicos Corregidos
                              │
                              ▼
                 Extracción de información
                              │
                              ▼
                  Vertical Data Science (VDS)
                              │
      ┌────────────────────────────────────────┐
      │                                        │
      │  • Estadística descriptiva             │
      │  • Visualización                       │
      │  • Correlaciones                       │
      │  • Clustering                          │
      │  • Caracterización de registros        │
      │                                        │
      └────────────────────────────────────────┘
                              │
                              ▼
              Evaluación de Compatibilidad Espectral
                              │
                              ▼
            Verificación de criterios normativos
                              │
                              ▼
             Selección de registros sísmicos
                              │
                              ▼
             Análisis No Lineal Tiempo-Historia
                              │
                              ▼
             Evaluación del desempeño estructural
                              │
                              ▼
          Derivas • Daño • Nivel de desempeño
```

---

# Variables de estudio

## Variable Independiente

**Registros sísmicos corregidos**

Dimensiones:

- Magnitud (Mw)
- PGA
- Profundidad
- Duración significativa
- Compatibilidad espectral
- Características del registro
- Representatividad del espectro objetivo

---

## Variable Dependiente

**Respuesta sísmica de la estructura**

Indicadores:

- Deriva máxima de entrepiso
- Desplazamiento máximo
- Cortante basal
- Nivel de desempeño
- Estado de daño (Hazus / ASCE 41)

---

# Tecnologías

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-Learn
- SciPy
- Jupyter Notebook

Software de Ingeniería:

- ETABS
- OpenSees *(opcional)*
- SAP2000 *(si aplica)*

---

# Estructura del Proyecto

```
 seismic-vds
│
├── data
│   ├── raw
│   ├── processed
│   └── spectra
│
├── notebooks
│
├── src
│   ├── preprocessing
│   ├── spectral_analysis
│   ├── clustering
│   ├── visualization
│   ├── nltha
│   └── utils
│
├── reports
│
├── figures
│
├── requirements.txt
│
└── README.md
```

---

# Fuente de Datos

Los registros acelerográficos utilizados en este proyecto provienen principalmente del:

**Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID)**

https://www.cismid.uni.edu.pe/ceois/redacis/red/

En caso de requerirse información complementaria, podrán emplearse registros oficiales del:

- Instituto Geofísico del Perú (IGP)

---

# Metodología

El desarrollo del proyecto contempla las siguientes etapas:

1. Recolección de registros sísmicos corregidos.
2. Organización y limpieza de la base de datos.
3. Caracterización mediante Vertical Data Science.
4. Evaluación de espectros de respuesta.
5. Verificación del cumplimiento de criterios normativos.
6. Selección de acelerogramas representativos.
7. Aplicación en análisis no lineal tiempo-historia.
8. Evaluación del desempeño estructural.

---

# Normativa y Referencias

- FEMA P-58
- Norma Técnica Peruana E.030 Diseño Sismorresistente
