import pandas as pd
import numpy as np

print("Unique Values, Value Counts, and Membership\n")
"""Another class of related methods extracts information about the values contained in a
one-dimensional Series."""

serie = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

print(serie)
print()
print(serie.unique())
print()
print(serie.value_counts())  # resumen de los elementos
print()

# isin performs a vectorized set membership check
mask = serie.isin(["b", "c"])
print(mask)
print()
# es util para el filtrado de una serie
print(serie[mask])


df = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                   'Qu2': [2, 3, 1, 2, 3],
                   'Qu3': [1, 5, 2, 4, 4]})

print(df)
print()
print(df.apply(pd.value_counts).fillna(0))
