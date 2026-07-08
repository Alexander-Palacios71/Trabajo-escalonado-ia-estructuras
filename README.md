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

## Descripción
El Perú se ubica en el Cinturón de Fuego del Pacífico, con la Zona Sísmica 3 (Norma E.030) entre las
regiones de mayor amenaza sísmica del país. Este proyecto aplica técnicas de **Vertical Data Science**
para caracterizar y seleccionar registros sísmicos corregidos, evaluando su aptitud para análisis no
lineales tiempo-historia y el desempeño sísmico de estructuras según criterios normativos internacionales.

## Fuente de datos
- Centro Peruano Japonés de Investigaciones Sísmicas y Mitigación de Desastres (CISMID)
- Instituto Geofísico del Perú (IGP), como complemento

## Variables

**Variable independiente:** Registros sísmicos corregidos evaluados mediante Vertical Data Science
- Características del registro
- Compatibilidad espectral
- Magnitud del evento
- Profundidad
- PGA
- Duración significativa
- Representatividad respecto al espectro objetivo

**Variable dependiente:** Respuesta sísmica de la estructura
- Deriva máxima de entrepiso
- Desplazamiento máximo
- Cortante basal
- Nivel de desempeño estructural
- Estado de daño según Hazus

## Estructura del repositorio
```
.
├── data/
│   ├── registros_sismicos.csv              # Dataset base (registros de la propuesta)
│   └── registros_sismicos_procesado.csv    # Generado por el notebook
├── notebooks/
│   └── 01_exploracion_registros_sismicos.ipynb
├── src/                                    # Scripts de procesamiento (próximas etapas)
├── TRABAJO_FINAL_1__2_.docx                # Documento de la propuesta
├── requirements.txt
└── README.md
```

## Cómo ejecutar

```bash
python3 -m venv venv
source venv/bin/activate          # En Windows: venv\Scripts\activate
pip install -r requirements.txt

jupyter notebook notebooks/01_exploracion_registros_sismicos.ipynb
```

## Próximos pasos
- Ampliar la muestra con más registros de CISMID / IGP.
- Calcular espectros de respuesta y evaluar compatibilidad espectral.
- Aplicar clustering / reducción de dimensionalidad (Vertical Data Science) para identificar patrones.
- Seleccionar registros aptos para análisis no lineal tiempo-historia.
- Exportar registros seleccionados a formato compatible con ETABS / OpenSees.
