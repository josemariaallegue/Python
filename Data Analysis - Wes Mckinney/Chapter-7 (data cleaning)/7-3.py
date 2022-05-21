import pandas as pd

print("Removing Duplicates\n")

df = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                   'k2': [1, 1, 2, 3, 3, 4, 4]})

print(df)
print()
# determinamos duplicados
print(df.duplicated())
print()
# filtramos por los duplicados
print(df[df.duplicated()])
print()
# quitamos duplicados
print(df.drop_duplicates())
print()
# quitarmos duplicados pero teniendo en cuenta los datos
# de un grupo determinado de columnas
print(df.drop_duplicates(["k1"]))
print()
# hacemos lo mismo que en punto anterior pero manteniendo el ultimo duplicaado
print(df.drop_duplicates(["k1"], keep="last"))
print()
