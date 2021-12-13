import pandas as pd
import numpy as np

print("Dropping Entries from an Axis\n")

serie = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

print(serie)
print()

print(serie.drop(["c", "a"]))
print()

df = pd.DataFrame(np.arange(16).reshape((4, 4)),
                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns=['one', 'two', 'three', 'four'])

print(df)
print()
print(df.drop((['Colorado', 'Ohio'])))
print()
print(df.drop('two', axis=1))  # axis=1 indica que se quiren eliminar columnas

# al poner true en inplace se modifica el objeto que la llama y no devuel nada
df.drop("two", axis=1, inplace=True)
