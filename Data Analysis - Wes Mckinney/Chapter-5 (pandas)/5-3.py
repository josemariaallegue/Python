import pandas as pd
import numpy as np

print("Sorting and Ranking\n")

serie = pd.Series([1, np.nan, -5, 5, -6], index=['d', 'a', 'b', 'c', "j"])

print(serie.sort_index())
print()
# Any missing values are sorted to the end of the Series by default
print(serie.sort_values(ascending=False))
print()

df = pd.DataFrame(np.arange(8).reshape((2, 4)),
                  index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])

print(df.sort_index())
print()
print(df.sort_index(axis=1))
print()
print(df.sort_index(axis=1, ascending=False))
print()

"""When sorting a DataFrame, you can use the data in one or more columns as the sort
keys."""
df2 = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})

print(df2)
print()
print(df2.sort_values(by='b'))
print()
print(df2.sort_values(by=['a', "b"]))
