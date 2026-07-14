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

# Descripción del dataset

El conjunto de datos utilizado estará conformado por registros acelerográficos correspondientes a eventos sísmicos ocurridos en el territorio peruano y almacenados en el repositorio del Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID). Dicho repositorio constituye una de las principales fuentes oficiales de información acelerográfica del país y reúne registros obtenidos mediante la Red Nacional de Acelerógrafos, proporcionando información indispensable para el análisis del comportamiento dinámico de estructuras sometidas a cargas sísmicas.
El sistema desarrollado establecerá una conexión con el repositorio para consultar y descargar automáticamente los registros seleccionados por el usuario mediante criterios de búsqueda previamente definidos, tales como año de ocurrencia, magnitud del evento, profundidad focal, estación acelerográfica, ubicación geográfica y otros parámetros disponibles en la base de datos.

# Volumen del dataset

El sistema no trabajará con un conjunto de datos estático, sino con un dataset dinámico, ya que los registros serán consultados y descargados directamente desde el repositorio del CISMID según los criterios de búsqueda definidos por el usuario. En consecuencia, el número de registros procesados podrá variar desde un único acelerograma hasta cientos de registros pertenecientes a distintos eventos sísmicos, dependiendo de las necesidades del estudio.

---

# Marco VDS
## Predictability

La predictibilidad no está asociada a la predicción de variables estructurales mediante modelos de inteligencia artificial, sino a la capacidad del sistema para producir resultados consistentes y técnicamente correctos a partir de registros sísmicos adquiridos desde el repositorio del CISMID.
Los algoritmos implementados deberán generar registros acelerográficos procesados cuya respuesta sea coherente con los principios físicos del movimiento sísmico y comparable con los resultados obtenidos mediante software especializados como SeismoSignal y SeismoMatch. En este sentido, la predictibilidad estará determinada por la capacidad del sistema para reproducir de manera automática procesos consolidados en la ingeniería sísmica, tales como la corrección de línea base, el filtrado digital, el cálculo de espectros de respuesta y el escalamiento espectral.
Por tanto, la predictibilidad se evaluará mediante la concordancia entre los resultados generados por la plataforma desarrollada y aquellos obtenidos con herramientas de referencia ampliamente utilizadas en la práctica profesional.

## Computability

La computabilidad hace referencia a la capacidad del sistema para ejecutar eficientemente todas las etapas del procesamiento de registros sísmicos utilizando recursos computacionales convencionales. El software será desarrollado en Python utilizando bibliotecas especializadas como NumPy, Pandas, SciPy, ObsPy, Plotly y Dash, las cuales permiten implementar algoritmos numéricamente estables y optimizados para el procesamiento de grandes volúmenes de datos científicos.
La arquitectura modular del sistema permitirá automatizar el flujo completo de trabajo, desde la consulta del repositorio del CISMID hasta la generación de registros corregidos y escalados, reduciendo significativamente el tiempo requerido para el procesamiento manual y permitiendo analizar múltiples registros de manera consecutiva sin intervención del usuario. En consecuencia, se espera que el sistema sea capaz de procesar lotes de registros acelerográficos manteniendo tiempos de ejecución adecuados y un uso eficiente de los recursos computacionales.

## Stability

La estabilidad representa uno de los principios más importantes dentro del presente proyecto, ya que busca garantizar que pequeñas variaciones en los datos de entrada o en los parámetros de procesamiento no produzcan cambios significativos en los resultados finales. Para ello, el sistema incorporará procedimientos automáticos de validación y control de calidad de los registros sísmicos antes de iniciar su procesamiento, verificando la existencia de valores nulos, inconsistencias en el intervalo de muestreo, registros incompletos y posibles anomalías instrumentales.
Asimismo, la estabilidad será evaluada verificando que los algoritmos de corrección de línea base, filtrado digital y cálculo espectral produzcan resultados consistentes al ser aplicados sobre diferentes registros sísmicos con características diversas, conservando las propiedades físicas esenciales de la señal y minimizando la aparición de desplazamientos residuales o distorsiones espectrales. Adicionalmente, la naturaleza determinística de los algoritmos implementados garantiza que un mismo registro procesado bajo idénticas condiciones genere siempre el mismo resultado, favoreciendo la reproducibilidad científica y la trazabilidad de los análisis realizados.

---

# Análisis Exploratorio de Datos (EDA)

En esta fase, el sistema desarrollado en Python realizará la adquisición automática de los registros sísmicos y de sus metadatos asociados, tales como fecha del evento, magnitud de momento (Mw), profundidad focal, ubicación del epicentro, estación acelerográfica, intervalo de muestreo, duración del registro y aceleración máxima del terreno (PGA). Posteriormente, se efectuará un proceso de depuración de la información mediante la identificación de registros incompletos, detección de valores nulos, verificación de inconsistencias en el formato de los archivos y eliminación de datos duplicados o que no cumplan con los criterios mínimos de calidad para su procesamiento.
Como parte del análisis exploratorio, se realizará una caracterización estadística de la base de datos, evaluando la distribución de variables como magnitud, profundidad, PGA, duración efectiva e intervalo de muestreo, con el propósito de identificar tendencias generales y posibles valores atípicos que puedan influir en el procesamiento posterior de las señales. Asimismo, se desarrollará un análisis de correlación entre las principales variables sísmicas, permitiendo estudiar la relación existente entre parámetros como la magnitud del evento, la profundidad hipocentral, la distancia epicentral, la aceleración máxima registrada y otros indicadores relevantes. Este análisis facilitará la comprensión del comportamiento de la base de datos y permitirá establecer criterios objetivos para la selección de registros destinados al análisis dinámico.
La información será complementada mediante visualizaciones interactivas desarrolladas con librerías especializadas de Python, tales como Pandas para la manipulación de datos, NumPy para el procesamiento numérico, Matplotlib y Plotly para la representación gráfica de las señales y de las variables estadísticas, así como Folium o Plotly Maps para la representación geoespacial de los eventos sísmicos sobre un mapa interactivo del Perú. La interfaz permitirá filtrar los registros por criterios como año de ocurrencia, magnitud, profundidad, departamento, estación acelerográfica y rango de aceleraciones registradas, facilitando la exploración de la información y la selección automática de los registros de interés. Finalmente, el EDA permitirá validar la calidad de la información antes de ejecutar las etapas de corrección de línea base, aplicación de filtros digitales, cálculo de espectros de respuesta y escalamiento espectral, garantizando que únicamente se procesen registros que satisfagan los criterios técnicos establecidos para el análisis sísmico.

---

# Plan de algoritmos

El sistema propuesto estará conformado por un conjunto de algoritmos determinísticos orientados al procesamiento digital de señales sísmicas y al análisis numérico, los cuales permitirán automatizar el tratamiento de registros acelerográficos obtenidos del repositorio del CISMID. Debido a que el objetivo del software consiste en acondicionar registros sísmicos para su posterior utilización en análisis dinámicos no lineales, no se requiere el entrenamiento de modelos de aprendizaje automático ni de redes neuronales, ya que el procesamiento se fundamenta en procedimientos físicos y matemáticos ampliamente establecidos en la ingeniería sísmica.

## Adquisición y organización de registros sísmicos

Se implementarán algoritmos para la consulta, extracción y gestión automatizada de la información contenida en el repositorio del CISMID, permitiendo la descarga sistemática de los registros acelerográficos junto con sus respectivos metadatos. Posteriormente, esta información será estructurada y organizada mediante el uso de la biblioteca Pandas, facilitando su almacenamiento, consulta, filtrado y procesamiento automatizado. Este procedimiento optimizará la eficiencia en la gestión de los datos, reducirá los errores asociados al procesamiento manual y garantizará la integridad, consistencia y trazabilidad de la información empleada durante el desarrollo de la investigación.

## Adquisición y organización de registros sísmicos

Antes del procesamiento de las señales acelerográficas, se implementarán algoritmos de limpieza y validación de datos con el propósito de verificar la calidad, integridad y consistencia de la información contenida en el repositorio. Estos algoritmos permitirán identificar y corregir posibles anomalías mediante la detección de:
 - Valores nulos.
 - Inconsistencias en el intervalo de muestreo.
 - Errores de formato.
La aplicación de este proceso garantizará que únicamente se incorporen al análisis registros válidos y consistentes, optimizando la calidad del conjunto de datos, reduciendo la propagación de errores durante las etapas posteriores de procesamiento y fortaleciendo la confiabilidad, reproducibilidad y trazabilidad de los resultados obtenidos.

## Corrección de línea base (Baseline Correction)

La corrección de la línea base se realizará mediante la implementación de algoritmos especializados para la eliminación de tendencias (detrending) y el ajuste polinomial, con el propósito de suprimir los desplazamientos residuales ocasionados por errores instrumentales y componentes de baja frecuencia presentes en las señales acelerográficas. Entre los métodos que se implementarán se incluyen:
 - Eliminación de la media.
 - Eliminación de tendencia lineal.
 - Ajuste polinomial de distintos órdenes.
La aplicación de estos procedimientos permitirá obtener señales correctamente referenciadas respecto a su línea base, minimizando la acumulación de errores durante la integración numérica de la aceleración para la obtención de velocidad y desplazamiento, mejorando así la precisión y confiabilidad de los resultados del procesamiento sísmico.

## Filtrado digital

Se implementará un filtro digital Butterworth de fase cero mediante el algoritmo Forward–Backward Filtering (filtfilt), con la finalidad de atenuar el ruido de alta y baja frecuencia presente en las señales acelerográficas sin introducir desfases ni distorsiones en su contenido temporal. La aplicación de este procedimiento permitirá preservar la fase original de la señal, mantener la estabilidad numérica del procesamiento y obtener registros con una mayor relación señal-ruido, garantizando así información más confiable para las etapas posteriores de análisis e interpretación de los datos sísmicos. 

## Integración numérica

La obtención de las historias de velocidad y desplazamiento se realizará mediante técnicas de integración numérica aplicadas a los registros acelerográficos previamente corregidos y filtrados, utilizando la regla trapezoidal acumulativa. Este procedimiento permitirá transformar de manera precisa las aceleraciones registradas en sus correspondientes respuestas cinemáticas, preservando la coherencia temporal de la señal y proporcionando parámetros fundamentales para el análisis dinámico y la evaluación del comportamiento estructural.

## Cálculo del espectro de respuesta

El cálculo del espectro elástico de respuesta se efectuará mediante la resolución de la ecuación dinámica de un sistema de un grado de libertad (SDOF), empleando el método de integración paso a paso de Newmark-β. A partir de este procedimiento se obtendrán los espectros de aceleración (Sa), velocidad (Sv) y desplazamiento (Sd) para los diferentes períodos de vibración considerados. La implementación de este método permitirá generar espectros con alta estabilidad numérica y precisión, constituyendo una base confiable para la caracterización de la demanda sísmica y su aplicación en el análisis y diseño estructural.

## Escalamiento espectral

Se implementará un algoritmo de escalamiento espectral automático que compare el espectro de respuesta del registro acelerográfico procesado con un espectro objetivo previamente definido, ya sea el espectro de diseño establecido en la Norma Técnica E.030 – Diseño Sismorresistente o un espectro específico correspondiente al proyecto de estudio. A partir de esta comparación se determinará el factor de escala requerido para ajustar la intensidad del registro sísmico. Asimismo, en etapas posteriores del desarrollo podrá incorporarse un algoritmo de ajuste espectral mediante la técnica de Wavelet Matching, similar a la empleada en programas especializados como SeismoMatch, con el propósito de lograr una mayor compatibilidad entre el espectro del registro procesado y el espectro objetivo, garantizando registros sísmicos adecuados para análisis dinámicos lineales y no lineales. 

## Visualización interactiva

Se desarrollarán algoritmos de visualización interactiva empleando las bibliotecas Plotly y Dash, con el propósito de representar de manera dinámica e intuitiva la información generada durante el procesamiento de los registros acelerográficos. Estas herramientas permitirán explorar, analizar y comparar los resultados obtenidos mediante gráficos interactivos y paneles de control, facilitando la interpretación de la información y el análisis de la respuesta sísmica.

---

# RESULTADO PREVISTOS

Se espera desarrollar una plataforma informática que automatice la adquisición, procesamiento y acondicionamiento de registros sísmicos del repositorio del CISMID, reduciendo la intervención manual y mejorando la eficiencia del procesamiento. Su desempeño será evaluado mediante indicadores técnicos que verifiquen la precisión de los algoritmos implementados y la calidad de los registros sísmicos procesados

## Error residual de línea base

Se evaluará la capacidad del algoritmo para eliminar tendencias espurias presentes en los registros acelerográficos mediante el análisis de los desplazamientos residuales obtenidos después de la integración numérica. Donde se espera obtener valores cercanos a cero, indicando una adecuada corrección de línea base y minimizando errores acumulativos durante la integración.

## Conservación de las características físicas del registro

Se verificará que los procedimientos de corrección y filtrado no alteren significativamente las características dinámicas originales de la señal sísmica. Las variaciones deberán mantenerse dentro de rangos técnicamente aceptables según los criterios utilizados en el procesamiento de registros sísmicos.

## Compatibilidad espectral

Se evaluará el grado de ajuste entre el espectro del registro procesado y el espectro objetivo definido por el usuario. Donde se deberá minimizar la diferencia entre ambos espectros dentro del rango de períodos de interés para análisis estructural.

## Eficiencia en el procesamiento automático

Se evaluará la capacidad del sistema para reducir el tiempo requerido para el acondicionamiento de registros sísmicos. Donde el criterio de éxito se evaluará: Reducción significativa respecto al procesamiento manual realizado mediante software independientes como SeismoSignal y SeismoMatch.

## Exactitud del cálculo espectral

Los espectros generados por el software serán comparados con resultados obtenidos mediante herramientas ampliamente utilizadas en ingeniería sísmica, tales como:
 - SeismoSignal
 - SeismoMatch
Donde se tendrá que obtener resultados equivalentes a los proporcionados por software especializados reconocidos en la comunidad científica.

---

# Resultado esperado global

 - Conectarse automáticamente al repositorio sísmico del CISMID.
 - Visualizar eventos sísmicos mediante mapas interactivos y filtros avanzados.
 - Descargar y organizar registros acelerográficos.
 - Ejecutar corrección de línea base y filtrado digital sin intervención manual.
 - Calcular espectros de respuesta mediante algoritmos numéricos validados.
 - Escalar registros respecto a un espectro objetivo.
 - Exportar automáticamente los registros procesados y sus parámetros asociados.

