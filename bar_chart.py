import pandas as pd
import matplotlib.pyplot as plt

# Abrir el archivo
df = pd.read_csv("C:/Users/MSI ERICK/Desktop/Proyectos varios/scrapper_pruebas/test_python/linkendin_jobs_scrapper/data/historico.csv", encoding='utf-8-sig')


# Crear variable ciudad y hacer conteo (podemos colocar date_last para filtrar por fecha)
city_count = df['ciudad'].value_counts()

city_count.head(3).plot(kind='bar', color='steelblue')
for pos, num in enumerate(city_count.head(3)):
    plt.text(pos, num*1.009, f'{num:,.0f}'.replace(',', '.'), ha='center', fontsize=10)
plt.title('Top 3 ciudades con más solicitudes')
plt.xlabel('Ciudad')
plt.ylabel('Número de solicitudes')
plt.xticks(rotation=45, ha='center')
plt.tight_layout()
plt.show()
