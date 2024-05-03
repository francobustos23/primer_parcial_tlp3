"""
Se proporcionará una lista de ventas mensuales y su tarea es realizar análisis básico
sobre estas ventas.

● Agrupa los datos por trimestre y calcula el total de ventas para cada trimestre.
● Filtrar y mostrar solo los meses donde las ventas superen 20000.
● Encontrar el mes con el mayor volumen de ventas y mostrar esta información.
● Calcular el promedio de ventas mensuales y mostrar esta información.
● Crea un DataFrame que incluya dos columnas una para los meses y otra para
el total de ventas de cada mes.

"""
#Importamos pandas
import pandas as pd
#Importamos matplotlib
import matplotlib.pyplot as plt

ventas_mensuales = [
    {"mes": "Enero", "total_ventas": 15000, "año": 2023},
    {"mes": "Febrero", "total_ventas": 18000, "año": 2023},
    {"mes": "Marzo", "total_ventas": 22000, "año": 2023},
    {"mes": "Abril", "total_ventas": 19000, "año": 2023},
    {"mes": "Mayo", "total_ventas": 25000, "año": 2023},
    {"mes": "Junio", "total_ventas": 28000, "año": 2023},
    {"mes": "Julio", "total_ventas": 32000, "año": 2023},
    {"mes": "Agosto", "total_ventas": 30000, "año": 2023},
    {"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
    {"mes": "Octubre", "total_ventas": 31000, "año": 2023},
    {"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
    {"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
    {"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
    {"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
    {"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
    {"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
    {"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
    {"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
    {"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
    {"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
    {"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
    {"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
    {"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
    {"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]

#Creamos el dataframe
ventas_df = pd.DataFrame(ventas_mensuales)

#Creamos un diccionario llamado meses que asocia el nombre de cada mes con su respectivo número.
#Para poder utilizarlo más adelante para calcular el trimestre al que pertenece cada mes.
meses = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
    "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}

#Agregamos una nueva columna llamada trimestre
#El cual indica el trimestre al que pertenece cada mes
ventas_df['trimestre'] = (ventas_df['mes'].apply(lambda x: meses[x.split()[0]]) - 1) // 3 + 1

#Agrupamos los datos por trimestre y calculamos el total de ventas para cada trimestre
ventas_por_trimestre = ventas_df.groupby('trimestre')['total_ventas'].sum()
print("Ventas por trimestre: ",ventas_por_trimestre) 

#Filtramos y mostramos solo los meses donde las ventas superen 20000.
meses_mayores_a_20000 = ventas_df[ventas_df['total_ventas'] > 20000]['mes']
print("Meses con ventas superiores a 20000: ",meses_mayores_a_20000)

#Encontrar el mes con el mayor volumen de ventas y mostrar esta información.
mes_max_ventas = ventas_df.loc[ventas_df['total_ventas'].idxmax()]['mes']
max_ventas = ventas_df['total_ventas'].max()
print("Mes con el mayor volumen de ventas:", mes_max_ventas, "con", max_ventas, "ventas")

#Calculamos el promedio de las ventas 
promedio_ventas_mensuales = ventas_df['total_ventas'].mean()
print("Promedio de ventas mensuales:", promedio_ventas_mensuales)

#Creamos un nuevo DataFrame que incluya dos columnas una para los meses y otra para
#el total de ventas de cada mes.
ventas_por_mes_df = ventas_df[['mes', 'total_ventas']]
print("Ventas por mes: ", ventas_por_mes_df)

"""
Basándote en el DataFrame creado, realiza un análisis de gráficos para visualizar la
tendencia de ventas a lo largo de los meses. Utiliza un gráfico de líneas donde el eje x
represente los meses y el eje y represente el total de ventas de cada mes.

"""

plt.plot(ventas_por_mes_df['mes'], ventas_por_mes_df['total_ventas'], color="purple", marker='.',markersize=8, 
         markerfacecolor="red") #Indicamos los valores que van a ir en los ejes
#mes en el eje x y total_ventas en el eje y
#le agregamos un color a la linea y un simbolo de marca (con sutamaño y color) 
plt.grid(True) #Le agregamos la cuadricula
plt.xlabel('Meses') #Nombre del eje x
plt.ylabel('Ventas') #Nombre del eje y
plt.title('Tendencia de ventas') #Titulo del grafico
plt.xticks(rotation=70) 
plt.show() #Mostramos la grafica despues de definir los elementos