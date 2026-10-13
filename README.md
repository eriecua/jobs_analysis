# Jobs Analysis

Este repositorio analiza ofertas de empleo para entender mejor el mercado laboral en Ecuador y, en particular, cómo se distribuyen los perfiles de trabajo por área, ciudad y tipo de puesto.

El objetivo principal es responder tres preguntas:

1. ¿Qué grupos de puestos se buscan con más frecuencia?
2. ¿Cómo se reparten esos puestos por ciudad?
3. ¿Qué títulos concretos forman cada grupo?

## ¿Qué hace este proyecto?

El flujo del proyecto es bastante sencillo:

- Lee un histórico de ofertas de empleo.
- Normaliza los nombres de los puestos (minúsculas, sin tildes, sin variaciones de escritura).
- Clasifica cada oferta en grupos como `Datos / BI`, `Produccion` o `Procesos`.
- Cuenta cuántas ofertas hay por grupo y por ciudad.
- Genera gráficos de barras y exporta una tabla resumen para análisis más avanzados.

Este tipo de análisis sirve para identificar tendencias del mercado laboral, detectar áreas con mayor demanda y preparar información útil para decisiones de carrera, contratación o análisis estratégico.

## Mapa del repositorio

| Archivo | Descripción |
|---|---|
| `job_analysis.py` | Script principal. Carga la data, clasifica los puestos, genera gráficos y exporta resultados. |
| `bar_chart.py` | Versión inicial o prueba del análisis visual. |
| `tabla_puestos.csv` | Resultado principal exportado: los puestos clasificados por grupo. |
| `requirements.txt` | Dependencias necesarias para ejecutar el proyecto. |
| `Analisis del mercado.png` | Resumen visual del análisis de mercado. |
| `README.md` | Documentación del proyecto. |

## Flujo de trabajo

1. Se carga el archivo de histórico de empleos.
2. Se normalizan los títulos para evitar errores por mayúsculas, tildes o variaciones en la redacción.
3. Se definen reglas de clasificación por palabra clave.
4. Se agrupan las ofertas por categoría y ciudad.
5. Se generan gráficos y exporta una tabla útil para Power BI, Excel o análisis posterior.

## Reglas de clasificación

Las categorías se definen por palabras clave, por ejemplo:

- `Datos / BI`: `data`, `datos`, `business intelligence`, `analista de datos`, `power bi`, etc.
- `Produccion`: `produccion` (excepto algunos casos como operadores).
- `Procesos`: `procesos`, `mejora`, `ingeniero industrial`, etc.

Todo lo que no coincide con esas reglas queda en `Sin clasificar` para evitar falsos positivos.

## Cómo correr el proyecto

Desde una terminal con Python instalado:

```bash
pip install -r requirements.txt
python job_analysis.py
```

Si estás usando PowerShell y un entorno virtual local:

```powershell
.venv\Scripts\Activate.ps1
python job_analysis.py
```

## Salidas esperadas

El proyecto genera:

- Un gráfico de ofertas por grupo.
- Un gráfico por ciudad con distribución por grupo.
- Un archivo `tabla_puestos.csv` listo para análisis en Excel o Power BI.

## Análisis de mercado

La imagen a continuación resume de forma visual el panorama del mercado laboral que este proyecto está evaluando:

![Análisis de mercado](./Analisis%20del%20mercado.png)

Este análisis busca facilitar la lectura del mercado para responder preguntas estratégicas como:

- ¿Qué perfiles tienen más demanda?
- ¿En qué ciudades se concentran más oportunidades?
- ¿Qué tipo de funciones están creciendo y cuáles están más saturadas?

## Observaciones importantes

- El proyecto depende del archivo histórico del scraper (`historico.csv`), que se actualiza con el tiempo.
- La ruta del archivo en `job_analysis.py` está codificada y puede requerir ajustes según el entorno local.
- El análisis es más valioso cuando se acumula más histórico, ya que permite detectar tendencias y no solo un punto de corte del mercado.

## Siguientes pasos recomendados

- Mejorar la preparación de datos y limpieza de títulos duplicados.
- Exportar reportes más estructurados para Excel o Power BI.
- Añadir análisis temporal para ver evolución mensual o trimestral.
- Crear dashboards más amigables para análisis de mercado y tendencias.

## Resumen ejecutivo

Este repositorio no solo clasifica ofertas, sino que ayuda a transformar una gran cantidad de información de empleos en una lectura más clara del mercado laboral. La combinación de clasificación, agrupación por ciudad y visualización facilita la toma de decisiones.
