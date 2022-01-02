import pandas as pd

print("Concatenating along an axis\n")

df1 = pd.DataFrame({"NOMBRE": ["JOSE", "PEPE", "JUAN", "CARLOS"],
                    "EDAD": [12, 13, 5, 2],
                    "ID": [123, 534, 1235, 7]})
df2 = pd.DataFrame({"NOMBRE": ["NOELI", "MARIA", "FLORENCIA", "CRISTINA"],
                    "EDAD": [76, 59,  43, 7],
                    "ID2": [144, 589, 15675, 345]})

print(df1)
print()
print(df2)
print()

# forma de concatenar series y dataframes
# se puede definir el axis
print(pd.concat([df1, df2], axis=0))
print()
# el tipo de join (outer or inner)
print(pd.concat([df1, df2], axis=0, join="inner"))
print()
# se puede descartar el index
print(pd.concat([df1, df2], axis=0, join="inner", ignore_index=True))
print()
# un identificar de donde proviene el dato
print(pd.concat([df1, df2], axis=0, join="inner",
      keys=["df1", "df2"], ignore_index=True))
print()
# si el axis es 1 los keys se convierten en columnas
print(pd.concat([df1, df2], axis=1, join="inner",
      keys=["df1", "df2"], ignore_index=True))
# equivalente al anterior
# print(pd.concat({"df1":df1, "df2":df2}, axis=1, join="inner",ignore_index=True))
