import pandas as pd
import numpy as np

print("Indexing, Selection, and Filtering\n")

serie = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

print(serie)
print()

print(serie["b"])
print()
print(serie[1])
print()
print(serie[[1, 2]])
print()
print(serie[serie < 2])
print()
print(serie[1:3])
print()
print(serie["a":"d"])  # slicin es inclusivo con el ultimo elemento
print()

serie["b":"c"] = 2020
print(serie["b":"c"])
print()


df = pd.DataFrame(np.arange(16).reshape((4, 4)),
                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns=['one', 'two', 'three', 'four'])


print(df)
print()
print(df["two"])
print()
print(df[["two", "one"]])
print()
print(df[:2])
print()
print(df[df["one"] > 5])
print()
print(df < 5)
print()
df[df < 5] = 0
print(df)
