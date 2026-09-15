# Data Análisis — Ofertas de empleo

Analiza el histórico de ofertas que genera el scraper de empleos
(`../scrapper_pruebas/test_python/linkendin_jobs_scrapper`) y responde tres preguntas:

1. ¿Qué grupos de puestos se buscan con más frecuencia?
2. ¿Cómo se reparten esos puestos por ciudad?
3. ¿Qué títulos concretos forman cada grupo?

## Archivos

| Archivo | Qué es |
|---|---|
| `job_analysis.py` | El análisis completo: clasificación, tablas, gráficos y exportación |
| `bar_chart.py` | Borrador original: top 3 ciudades con más ofertas |
| `tabla_puestos.csv` | **Salida**: cada puesto clasificado con su grupo (listo para Power BI) |
| `requirements.txt` | Dependencias del entorno |
| `.venv/` | Entorno propio de esta carpeta (Python 3.11, pandas, matplotlib) |

## Cómo correr

Desde PowerShell, activando el entorno de la carpeta:

```powershell
.venv\Scripts\Activate.ps1
python job_analysis.py
```

Abre dos ventanas de gráficos y escribe `tabla_puestos.csv` en esta carpeta.

## De dónde salen los datos

La constante `RUTA` (línea 5 de `job_analysis.py`) apunta al `historico.csv` del
scraper. Ese CSV crece solo: el scraper corre programado 3 veces al día, así que
los números del análisis cambian de un día para otro. Normal.

## Cómo se clasifican los puestos

Cada título se **normaliza** antes de comparar (minúsculas + sin tildes), para que
`Producción`, `PRODUCCION` y `produccion` cuenten como la misma palabra.

Reglas por grupo — el orden importa (el último que escribe gana):

| Prioridad | Grupo | Contiene | Excluye |
|---|---|---|---|
| 3 (gana) | Datos / BI | data, datos, data analysis, business intelligence, analista de datos, analista bi, business analyst | — |
| 2 | Produccion | produccion | operador |
| 1 | Procesos | procesos, analista de procesos, mejora, ingeniero industrial | — |

Todo lo demás queda como `Sin clasificar` (~4.200 ofertas: vendedores, asesores
comerciales, etc. — no son el foco del análisis).

## Qué produce

- **Gráfico 1**: ofertas por grupo (barras con etiquetas).
- **Gráfico 2**: ofertas clasificadas por ciudad, apiladas por grupo. Solo las
  3 ciudades de la constante `CIUDADES` (`Quito`, `Guayaquil`, `Santo Domingo`).
- **`tabla_puestos.csv`**: puestos × grupos (codificación `utf-8-sig` para que
  Excel muestre bien los acentos).
- **`tablas_ofertas.xlsx`**: 3 hojas (Puestos / Ciudades / Grupos) — *pendiente de
  escribir el bloque `pd.ExcelWriter`*.

## Cosas que quedan pendientes

- [ ] Escribir el bloque de `pd.ExcelWriter` (Excel de 3 hojas; requiere `openpyxl`)
- [ ] Limpiar títulos duplicados con numeración de spam (`175. Senior Data Engineer`,
      `176. Senior Data Engineer` — el spam de LinkedIn que ya documentó el scraper)
- [ ] Exportar datos limpios para Power BI
- [ ] Predicción de tendencias (ML) — requiere más histórico acumulado primero
