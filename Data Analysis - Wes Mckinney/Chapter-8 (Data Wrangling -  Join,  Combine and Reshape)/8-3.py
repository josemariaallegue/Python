import pandas as pd

print("Indexing with a DataFrame’s columns\n")

df = pd.DataFrame({'a': range(7),
                   'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})

print(df)
print()
# trasnsposicion completa
print(df.T)
print()
# seteo de index a partir de columnas
print(df.set_index(["c", "d"]))
print()
# se pueden dejar las columnas si se quiere
print(df.set_index(["c", "d"], drop=False))
print()
# rese_index ubica los "nuevos" indexes en las columnas
# df.reset_index()
