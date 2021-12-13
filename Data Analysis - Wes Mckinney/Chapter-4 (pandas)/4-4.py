import pandas as pd
import numpy as np

print("Reindexing\n")

# reindex permite reorganizar una serie o df a parir de un array
# si en el nuevo index se pusiera alguno que no exista se ponen NaN como valor
serie = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

print(serie)
print()

print(serie.reindex(['a', 'b', 'c', 'd', 'e']))

# ffill permite rellenar una serie o df con los index faltantes repitiendo los elementos anteriores
serie2 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

print(serie2)
print()

print(serie2.reindex(range(6), method="ffill"))
print()

# reindex en df
df = pd.DataFrame(np.arange(9).reshape((3, 3)),
                  index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])

print(df)
print()
print(df.reindex(['a', 'b', 'c', 'd']))  # reindex en las filas
print()
# reindex de las columnas
print(df.reindex(columns=['Texas', 'Utah', 'California']))
print()
