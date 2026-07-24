# Selección y Corrección de Registros Sísmicos Mediante Veridical Data Science para Análisis No Lineales Tiempo-Historia de Estructuras del Perú

**Autores:** Alexander Ítalo Palacios Rojas, Jhon Franklin Cristobal Villanueva, Gisela Shenna Quintana Huayta, José Gustavo Segura Sanchez  
**Afiliación:** Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID) | Facultad de Ingeniería Civil, Universidad Nacional de Ingeniería (UNI)  
**Docente:** Kurt Walter Soncco Sinchi  
**Fecha:** Julio, 2026  

---

## 📑 Resumen

El análisis dinámico no lineal tiempo-historia constituye una de las metodologías más rigurosas para evaluar el comportamiento sísmico de estructuras, cuya confiabilidad depende directamente de la calidad y representatividad de los registros acelerográficos empleados como excitación dinámica. En la práctica profesional, el acondicionamiento de estos registros continúa realizándose mediante procedimientos predominantemente manuales y el uso de múltiples aplicaciones independientes, lo que incrementa el tiempo de procesamiento, dificulta la trazabilidad del análisis y aumenta la probabilidad de errores operativos.

En respuesta a esta problemática, el presente estudio propone el desarrollo de una plataforma computacional integrada, implementada en Python, capaz de automatizar el flujo completo de procesamiento de registros sísmicos provenientes del repositorio del Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID). La plataforma incorpora procesos automatizados de adquisición, depuración, selección, corrección de línea base, filtrado digital, cálculo de espectros de respuesta y escalamiento espectral, integrados bajo el enfoque metodológico de **Veridical Data Science (VDS)**.

Asimismo, el sistema combina algoritmos determinísticos de procesamiento digital de señales con técnicas de inteligencia artificial orientadas a optimizar la selección de registros compatibles con los requerimientos del análisis estructural. Se espera que esta herramienta reduzca significativamente la intervención manual, mejore la reproducibilidad de los resultados y proporcione registros acelerográficos técnicamente validados para su aplicación en análisis dinámicos no lineales, contribuyendo al fortalecimiento de la ingeniería sismorresistente y al desarrollo de herramientas computacionales especializadas para la evaluación del desempeño estructural en el Perú.

**Palabras clave:** *Veridical Data Science, registros acelerográficos, análisis dinámico no lineal tiempo-historia, CISMID, procesamiento digital de señales, espectro de respuesta, ingeniería sismorresistente, Python.*

---

## I. INTRODUCCIÓN

En la ingeniería estructural moderna, el análisis dinámico no lineal Tiempo-Historia constituye uno de los procedimientos más rigurosos para evaluar la respuesta sísmica y el desempeño de edificaciones e infraestructura frente a eventos sísmicos severos. La confiabilidad de este tipo de análisis depende, en gran medida, de la calidad de los registros acelerográficos utilizados como excitación sísmica, los cuales deben ser previamente acondicionados mediante procesos de corrección de línea base, filtrado digital y escalamiento espectral para garantizar que representen adecuadamente las características del movimiento del terreno y cumplan con los criterios normativos vigentes [1], [2].

Actualmente, este acondicionamiento se realiza principalmente mediante softwares especializados, como SeismoSignal y SeismoMatch [3], lo que implica un proceso predominantemente manual. Este flujo de trabajo requiere descargar los registros desde repositorios sísmicos, verificar su calidad, ejecutar individualmente la corrección, generar los espectros, escalar y exportar los resultados. Este procedimiento demanda un tiempo considerable, depende de la experiencia del usuario y aumenta la posibilidad de errores, especialmente con un número elevado de registros.

Adicionalmente, repositorios como el administrado por el Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID) contienen una vasta cantidad de información distribuida en múltiples eventos y formatos [4]. La ausencia de herramientas integradas que permitan consultar y procesar automáticamente esta información dificulta la selección de registros compatibles. Como consecuencia, los ingenieros invierten tiempo valioso en actividades repetitivas de gestión de datos en lugar de concentrarse en la evaluación del desempeño estructural.

En este contexto, se plantea desarrollar una plataforma computacional que integre en un único entorno de trabajo la consulta automática del repositorio sísmico, la visualización interactiva, la selección mediante filtros técnicos y el procesamiento completo de la señal. Con ello se busca mejorar la eficiencia, minimizar errores y proporcionar registros procesados con calidad técnica adecuada bajo la normativa peruana E.030 [5].

---

## II. METODOLOGÍA

### A. Descripción y Volumen del Dataset
El conjunto de datos utilizado está conformado por registros acelerográficos correspondientes a eventos sísmicos ocurridos en territorio peruano, los cuales fueron previamente descargados del repositorio del Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID) [4] para conformar una base de datos local. La cantidad exacta de registros que componen este dataset de trabajo es de **[INSERTAR CANTIDAD EXACTA]**.

A partir de este conjunto de datos estático, los registros son consultados y filtrados localmente por el sistema mediante criterios de búsqueda definidos por el usuario (tales como año de ocurrencia, magnitud, profundidad focal, estación y ubicación geográfica). En consecuencia, el volumen de datos procesado en cada ejecución puede variar desde un único acelerograma hasta cientos de registros de distintos eventos, dependiendo estrictamente de los filtros aplicados y las necesidades específicas del estudio estructural.

### B. Marco Veridical Data Science (VDS)
El desarrollo de la plataforma se rige por los tres principios fundamentales del marco VDS:
1. **Predictability (Predictibilidad):** Capacidad del sistema para producir resultados consistentes y técnicamente correctos, reproduciendo automáticamente procesos consolidados en ingeniería sísmica (corrección de línea base, filtrado, etc.) que sean comparables con softwares de referencia como SeismoSignal y SeismoMatch [3].
2. **Computability (Computabilidad):** Ejecución eficiente de todas las etapas utilizando recursos convencionales. El software se desarrolla en Python (utilizando librerías científicas como `NumPy`, `Pandas`, `SciPy` y `ObsPy`) con una arquitectura modular que permite procesar lotes de registros consecutivamente y sin intervención del usuario.
3. **Stability (Estabilidad):** Garantía de que variaciones menores en los datos no produzcan cambios drásticos en los resultados. Se incorporan validaciones de calidad (detección de nulos, consistencia de muestreo) y se asegura que algoritmos como el filtrado minimicen distorsiones espectrales. La naturaleza determinística de los procesos garantiza una reproducibilidad exhaustiva.

### C. Análisis Exploratorio de Datos (EDA)
Se realiza la adquisición automática de metadatos (fecha, magnitud $M_w$, profundidad, PGA, entre otros) y una depuración de información para eliminar datos corruptos o duplicados. Mediante análisis estadístico y de correlación de variables, se establecen criterios objetivos de selección. Esta etapa incluye visualizaciones interactivas espaciales (mapas del Perú) y gráficas de las señales en el dominio del tiempo utilizando las librerías `Plotly` y `Pandas`.

### D. Plan de Algoritmos y Procesamiento Digital
El núcleo computacional comprende algoritmos determinísticos y un modelo de inteligencia artificial:
*   **Selección por Redes Neuronales:** Un modelo procesa un número $n$ de registros, acondicionándolos y seleccionando automáticamente los siete más adecuados para el análisis estructural basándose en compatibilidad espectral normativa [5].
*   **Gestión Automatizada:** Extracción estructurada desde el CISMID utilizando esquemas de datos optimizados en `Pandas`.
*   **Corrección de Línea Base:** Eliminación de tendencias (*detrending*) y ajuste polinomial para suprimir desplazamientos residuales y errores instrumentales [1].
*   **Filtrado Digital:** Aplicación de un filtro Butterworth de fase cero (mediante el algoritmo `filtfilt` de `SciPy`) para atenuar el ruido de alta y baja frecuencia sin introducir desfases en la señal temporal.
*   **Integración Numérica:** Uso de la regla trapezoidal acumulativa para obtener las historias temporales de velocidad y desplazamiento del terreno.
*   **Cálculo Espectral:** Resolución de la ecuación dinámica de movimiento para un sistema de un grado de libertad (SDOF) mediante el método numérico de Newmark-$ eta$ [6], permitiendo obtener espectros de aceleración ($S_a$), velocidad ($S_v$) y desplazamiento ($S_d$).
*   **Escalamiento Espectral:** Comparación y ajuste de la intensidad del registro procesado frente al espectro objetivo de la Norma Técnica Peruana E.030 [5], con miras a implementar técnicas de *Wavelet Matching* para una mayor compatibilidad espectral en rangos de periodos estructurales clave.

---

## III. RESULTADOS PREVISTOS Y DISCUSIÓN

La plataforma informática será evaluada según rigurosos indicadores técnicos de desempeño cuantitativo y cualitativo, los cuales se resumen y estructuran en la Tabla I.

### Tabla I: Indicadores Técnicos de Evaluación de la Plataforma

| Indicador Técnico | Criterio de Evaluación / Meta | Herramienta de Control |
| :--- | :--- | :--- |
| **Error residual de línea base** | Desplazamientos residuales post-integración tendientes a cero ($d_{res} \approx 0$). | Integración numérica trapezoidal |
| **Conservación física** | Preservación de la dinámica original sin distorsión de fase ni atenuación anómala. | Filtro Butterworth fase cero (`scipy.signal.filtfilt`) |
| **Compatibilidad espectral** | Minimización del error medio cuadrático respecto al espectro objetivo E.030. | Método Newmark-$ eta$ / Escalamiento |
| **Eficiencia operativa** | Reducción drástica del tiempo de acondicionamiento por lote ($\ge 80\%$ de ahorro). | Procesamiento automatizado en Python |
| **Exactitud Algorítmica** | Equivalencia numérica ($R^2 \ge 0.98$) frente a softwares comerciales. | SeismoSignal y SeismoMatch |

Como resultado global, el ingeniero estructural podrá visualizar eventos, descargar lotes, corregir señales, calcular espectros, escalar y exportar resultados en un flujo unificado y validado científicamente. La adopción de los principios de Veridical Data Science garantiza que cada paso procesal sea auditable, eliminando la "caja negra" común en herramientas dispersas y asegurando que las decisiones de diseño estructural se basen en excitaciones sísmicas veraces y fidedignas.

---

## IV. CONCLUSIONES

1. La implementación de una herramienta automatizada basada en Python para el procesamiento de registros sísmicos del CISMID representa un avance significativo para la práctica y la investigación estructural en el Perú. Al delegar las tareas repetitivas y operativas a algoritmos rigurosos bajo el marco de Veridical Data Science, se mitiga el error humano, se asegura la reproducibilidad técnica y se optimiza el tiempo de desarrollo de los proyectos.
2. La integración de redes neuronales para la selección óptima de registros dota al ingeniero de recursos de alta confiabilidad para ejecutar análisis dinámicos no lineales acordes a las exigencias normativas nacionales e internacionales.
3. La integración de técnicas de procesamiento digital de señales e inteligencia artificial contribuirá a reducir la intervención manual, mejorar la reproducibilidad de los resultados y aumentar la confiabilidad de los registros utilizados en análisis dinámicos no lineales tiempo-historia.
4. La herramienta propuesta fortalecerá la eficiencia del análisis sísmico en ingeniería estructural, proporcionando un entorno computacional unificado para el tratamiento de registros acelerográficos y contribuyendo al desarrollo de herramientas tecnológicas aplicadas a la ingeniería sismorresistente en el Perú.

---

## 📚 REFERENCIAS

* [1] D. M. Boore, "Effect of baseline corrections on displacements and response spectra for several recordings of the 1999 Chi-Chi, Taiwan, earthquake," *Bulletin of the Seismological Society of America*, vol. 91, no. 5, pp. 1199–1211, 2001.
* [2] A. K. Chopra, *Dynamics of Structures: Theory and Applications to Earthquake Engineering*, 5th ed. Hoboken, NJ, USA: Pearson, 2020.
* [3] Seismosoft, "SeismoSignal and SeismoMatch - User Manuals," Pavia, Italy, 2025. [Online]. Available: https://seismosoft.com
* [4] Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID), "Repositorio de registros acelerográficos del Perú," Universidad Nacional de Ingeniería, Lima, Perú. [Online]. Available: http://www.cismid.uni.edu.pe
* [5] Ministerio de Vivienda, Construcción y Saneamiento, "Norma Técnica E.030: Diseño Sismorresistente," en *Reglamento Nacional de Edificaciones (RNE)*, Lima, Perú, 2024.
* [6] N. M. Newmark, "A method of computation for structural dynamics," *Journal of the Engineering Mechanics Division, ASCE*, vol. 85, no. 3, pp. 67–94, 1959.
