import pandas as pd
import numpy as np

print("loc and iloc\n")

"""They enable you to select a subset of the rows and columns from a
DataFrame with NumPy-like notation using either axis labels (loc) or integers
(iloc)."""

df = pd.DataFrame(np.arange(16).reshape((4, 4)),
                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns=['one', 'two', 'three', 'four'])

print(df)
print()
print(df.loc["Colorado", ["one", "two"]])  # con nombres
print()
print(df.iloc[1, [0, 1]])  # con numeros
print()
print(df.iloc[[1, 2], [3, 0, 1]])
print()
print(df.loc[:"Colorado", ["one"]])  # con slices
print()
print(df.iloc[:, :3][df.three > 5])  # con condicion
print()
