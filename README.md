# TF1: Propuesta de Datos - Aplicaciones de IA en Estructuras

## Título de investigación
Selección y evaluación de registros sísmicos corregidos mediante Veridical Data Science
para análisis no lineales tiempo-historia de estructuras ubicadas en la Zona Sísmica 3 del Perú.

## Integrantes
- Palacios Rojas Alexander Ítalo
- Cristobal Villanueva Jhon Franklin
- Quintana Huayta Gisela Shenna
- Segura Sanchez José Gustavo

## Docente
Kurt Walter Soncco Sinchi — Julio, 2026

# Problema de ingeniería estructural

En la ingeniería estructural moderna, el análisis dinámico no lineal Tiempo Historia constituye uno de los procedimientos más rigurosos para evaluar la respuesta sísmica y el desempeño de edificaciones e infraestructura frente a eventos sísmicos severos. La confiabilidad de este tipo de análisis depende, en gran medida, de la calidad de los registros acelerográficos utilizados como excitación sísmica, los cuales deben ser previamente acondicionados mediante procesos de corrección de línea base, filtrado digital y escalamiento espectral para garantizar que representen adecuadamente las características del movimiento del terreno y cumplan con los criterios establecidos por la normativa vigente.
Actualmente, este acondicionamiento se realiza principalmente mediante software especializados, como SeismoSignal y SeismoMatch, lo que implica un proceso predominantemente manual que requiere descargar los registros desde repositorios sísmicos, verificar su calidad, ejecutar individualmente la corrección de línea base, aplicar filtros digitales, generar los espectros de respuesta, realizar el escalamiento respecto a un espectro objetivo y exportar los resultados para su utilización en programas de análisis estructural. Este procedimiento demanda un tiempo considerable, depende de la experiencia del usuario y aumenta la posibilidad de errores durante la manipulación de la información, especialmente cuando se trabaja con un número elevado de registros sísmicos.
Adicionalmente, los repositorios de registros acelerográficos, como el administrado por el Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID), contienen una gran cantidad de información distribuida en múltiples eventos, estaciones acelerográficas y formatos de almacenamiento. La ausencia de herramientas integradas que permitan consultar, filtrar, visualizar y procesar automáticamente esta información dificulta la selección de registros compatibles con las características del análisis estructural y limita la eficiencia de los estudios de respuesta sísmica.
Como consecuencia, los ingenieros estructurales invierten una parte importante del tiempo de desarrollo de un proyecto en actividades repetitivas de búsqueda, organización y procesamiento de datos, en lugar de concentrarse en la interpretación de los resultados y la evaluación del desempeño estructural. Esta situación representa una limitación tanto para la investigación como para la práctica profesional, especialmente en estudios que requieren procesar múltiples registros sísmicos para cumplir con los procedimientos de análisis dinámico establecidos en normas nacionales e internacionales.
En este contexto, se plantea desarrollar una plataforma computacional que integre, en un único entorno de trabajo, la consulta automática del repositorio sísmico, la visualización interactiva de los eventos registrados, la selección de registros mediante filtros técnicos, la corrección de línea base, el filtrado digital, el cálculo de espectros de respuesta y el escalamiento espectral, automatizando el flujo completo de acondicionamiento de registros acelerográficos. Con ello se busca mejorar la eficiencia del proceso, reducir la intervención manual, minimizar errores operativos y proporcionar registros procesados con calidad técnica adecuada para su utilización en análisis dinámicos no lineales de estructuras.

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

- Visual Code

Software de Ingeniería:

- ETABS

---

## Aplicación de los principios de Vertical Data Science (PCS Framework)

### Predictibilidad (Predictability)

Los registros sísmicos corregidos contienen variables físicas medibles que permiten caracterizar el movimiento sísmico y seleccionar acelerogramas representativos. Se espera que estas características permitan predecir de manera consistente la respuesta estructural obtenida mediante análisis no lineal tiempo-historia, especialmente en términos de derivas y niveles de desempeño.

### Computabilidad (Computability)

La base de datos de registros sísmicos puede procesarse mediante herramientas computacionales de ciencia de datos, permitiendo realizar análisis estadísticos, verificación de criterios normativos, cálculo de espectros de respuesta, clasificación de registros y su posterior utilización en software de análisis estructural como ETABS, OpenSees o similares.

### Estabilidad (Stability)

Se espera que los patrones identificados y la selección de registros sean consistentes ante pequeñas variaciones en el conjunto de datos o en los parámetros de análisis, siempre que se mantengan los criterios normativos de selección. Asimismo, la metodología busca que la respuesta estructural obtenida sea representativa y reproducible para registros con características sísmicas similares de la Zona Sísmica 3 del Perú.

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
