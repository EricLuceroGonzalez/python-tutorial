import pandas as pd

data = {
    'Nombre': ['Pedro', 'María', 'Juan', 'Ana', 'Lily'],
    'Edad': [25, 30, 22, 35,17],
    'Puntuación': [85, 90, 88, 78,100]
}

df = pd.DataFrame(data)
print(df)

df_sorted_puntos = df.sort_values(by='Puntuación', ascending=False)
print(df_sorted_puntos)
primer_valor_puntuacion = df_sorted_puntos['Puntuación'].iloc[0]
print("\nPrimer valor de la columna 'Puntuación':", primer_valor_puntuacion)


df_sorted_edad = df.sort_values(by='Edad', ascending=False)
primer_valor_edad = df_sorted_edad['Edad'].iloc[0]
print("\nPrimer valor de la columna 'Edad':", primer_valor_edad)
print(df_sorted_edad)