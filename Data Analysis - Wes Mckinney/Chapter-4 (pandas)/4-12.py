import pandas as pd
import numpy as np

print("Axis Indexes with Duplicate Labels\n")
"""While many pandas functions (like reindex) require that the labels be
unique, it’s not mandatory."""

serie = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])

print(serie)
print()

# averiguar si hay index duplicados
print(serie.index.is_unique)
print()

"""Indexing a label with multiple entries returns a Series, while single entries return a
scalar value"""
print(serie["a"])
print()
print(serie["c"])
print()

df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])

print(df)
print()
print(df.loc["a"])
print()
