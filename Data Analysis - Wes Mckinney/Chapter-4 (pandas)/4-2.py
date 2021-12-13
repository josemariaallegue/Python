import pandas as pd
import numpy as np

print("Dataframes\n")
"""A DataFrame represents a rectangular table of data and contains an ordered collec‐
tion of columns, each of which can be a different value type (numeric, string,
boolean, etc.). The DataFrame has both a row and column index; it can be thought of
as a dict of Series all sharing the same index"""

# creacion a partir de un diccionario de listas de igual largo
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

# columns permite establecer el orden
df = pd.DataFrame(data, columns=["year", "state", "pop"])

print(df)
print()
print(df.head())  # primeros 5 elementos
print()
print(df.columns)  # solo las columnas
print()

# formas de obtener una serie a traves de un dataframe
# la primer forma es mas conveniente ya que si el nombre de la columna no es valido para python
# se genera un error con el segundo metodo
print(df.year)
print()
print(df["year"])
print()

# obtencion de filas con loc
print(df.loc[3])
print()

# creacion de columna y de valor a todas las filas
# se pueden insertar array, series, constantes
df["debt"] = np.arange(6.)
print(df)
print()

# eliminacion de una columna
df["aux"] = "aux"
print(df)
print()
del df["aux"]
print(df)
print()
