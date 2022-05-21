import pandas as pd
import numpy as np

print("Dataframes part 2\n")

# creacion de un df a partir de un diccionario de diccionarios
# los keys de primer nivel son la columnas y las de segundo nivel son los index
data = {'Nevada': {2001: 2.4, 2002: 2.9},
        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

df = pd.DataFrame(data)
print(df)
print()
print(df.T)  # transponer columnas con index
print()

# seteo de nombre de index y columnas
df.index.name = "year"
df.columns.name = "state"
print(df)
print()

# impresion de solo los valores
print(df.values)
print()
