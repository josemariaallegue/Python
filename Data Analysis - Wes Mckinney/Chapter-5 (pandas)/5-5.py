import pandas as pd
import numpy as np

print("Summarizing and Computing Descriptive Statistics\n")
"""pandas objects are equipped with a set of common mathematical and statistical meth‐
ods."""

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])

print(df)
print()
print(df.sum(axis=0))  # suma de columnas
print()
print(df.sum(axis=1))  # suma de filas
print()
# skipna permite tener en cuenta o no los NaN
print(df.sum(axis=1, skipna=False))
print()
# idmax permite determinar en que fila se encuentra el mayor valor
print(df.idxmax())
print()
print(df.cumsum(axis=0))  # para determinar la suma acumulada por fila
print()
print(df.describe())  # describe produce un resumen
print()
