import matplotlib.pyplot as plt
import pandas as pd

# Cargar el archivo
RUTA = "C:/Users/MSI ERICK/Desktop/Proyectos varios/scrapper_pruebas/test_python/linkendin_jobs_scrapper/data/historico.csv"

df = pd.read_csv(RUTA, encoding="utf-8-sig")

# Elegimos la columna title, y la pasamos a miniscula
titulos = df['title'].str.lower()
# ¿Cuales títulos contienen la palabra datos? True/False x fila
con_datos = titulos.str.contains('datos')

# Quitamos las tildes en 3 pasos.
titulos_norm = (
    df['title']
    # Todo minusculas
    .str.lower()
    # Todo sin tilde
    .str.normalize('NFKD')
    # Todas las tildes fuera de la cadena
    .str.encode('ascii', 'ignore')
    # Recuperamos el texto
    .str.decode('ascii')
)

# --- Datos / BI : relacionado a datos ---
es_datos = (
    titulos_norm.str.contains('data')
    | titulos_norm.str.contains('datos')
    | titulos_norm.str.contains('data analysis')
    | titulos_norm.str.contains('business intelligence')
    | titulos_norm.str.contains('analista de datos')
    | titulos_norm.str.contains('analista bi')
    | titulos_norm.str.contains('business analyst')
)
# --- Produccion: relacionado a industrias ---
es_produccion = (
    titulos_norm.str.contains('produccion')
    & ~titulos_norm.str.contains('operador') # quitamos a los operadores de máquinas.
)
# --- Procesos: relacionado a ingenieria ---
es_procesos = (
    titulos_norm.str.contains('procesos')
    | titulos_norm.str.contains('analista de procesos')
    | titulos_norm.str.contains('mejora')
    | titulos_norm.str.contains('ingeniero industrial')
)

# Todas las ofertas pasan sin clasificar
df['grupo'] = 'Sin clasificar'

# Reescribimos el cajón de las que SÍ encajan
df.loc[es_procesos, 'grupo'] = 'Procesos'
df.loc[es_produccion, 'grupo'] = 'Produccion'
df.loc[es_datos, 'grupo'] = 'Datos / BI'

# Contamos la columna grupo y QUITAMOS con .drop 'Sin clasificar':
conteo = df['grupo'].value_counts()
top = conteo.drop('Sin clasificar')

# Dentro del DataFrame de ciudad ponga los NA como 'Sin especificar'
df['ciudad'] = df['ciudad'].fillna('Sin especificar')

# Cruzar tablas (Como en tablas dinamicas de excel):
tabla = pd.crosstab(df['ciudad'], df['grupo'])
solo_grupos = tabla.drop(columns='Sin clasificar')

# Ciudades con AL MENOS 1 oferta clasificada (el resto son puros ceros)
con_ofertas = solo_grupos[solo_grupos.sum(axis=1) > 0]

CIUDADES = ['Quito', 'Guayaquil', 'Santo Domingo']

top_ciudades = con_ofertas[con_ofertas.index.isin(CIUDADES)]
print(top_ciudades)

# ================= Objetivo 3  =================
clasificadas = df[df['grupo'] != 'Sin clasificar']
tabla_puestos = pd.crosstab(clasificadas['title'], clasificadas['grupo'])
# Exportar a csv
tabla_puestos.index.name = 'Puesto'
tabla_puestos.to_csv('tabla_puestos.csv', encoding='utf-8-sig')



# Dibujamos el bar_chart, ahora con 'ax'
# ================= GRAFICO 1: por grupo (Objetivo 1) =================
ax = top.plot(kind='bar', color='steelblue')
for pos, num in enumerate(top):
    ax.text(pos, num+1, str(num), ha='center', fontsize=10)

ax.set_title('Ofertas por grupos')
ax.set_xlabel('Grupos de puestos')
ax.set_ylabel('Número de ofertas')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()

# ================= GRAFICO 2: por ciudad (Objetivo 2) =================
ax2 = top_ciudades.plot(
    kind='bar',
    stacked=True, # <--- barras apiladas
    color=['steelblue', 'orange', 'mediumseagreen']
) # Aqui podemos poner top_ciudades o con_ofertas

for contenedor in ax2.containers: # type: ignore
    ax2.bar_label(contenedor, label_type='center', fontsize=10) # type: ignore
ax2.set_title('Ofertas clasificadas por ciudad')
ax2.set_xlabel('Ciudad')
ax2.set_ylabel('Número de ofertas')
ax2.tick_params(axis='x', rotation=45)
plt.tight_layout()

# ================= AL FINAL: mostrar TODAS las ventanas =================
plt.show()




''' Objetivo: Buscar que puestos se estan buscando con mas frecuencia ''' "Listo ✅"
''' Objetivo 2: Hacer que cuente por ciudad'''  "Listo ✅"
''' Objetivo 3: Ver como tablas que puesto, ver tabla combinada los titulos que se estan filtrando''' "Listo ✅"
''' Limpieza y exportacion de datos limpios para powerbi ''' 
''' Hacer ML de hacia donde se van a mover la ofertas en los proximos 3 meses'''
''' Por Grupo, por Ofertas, por Ciudad'''