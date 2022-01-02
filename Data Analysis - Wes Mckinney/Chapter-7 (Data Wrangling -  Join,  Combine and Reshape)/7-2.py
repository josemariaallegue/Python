import numpy as np
import pandas as pd

print("Reordering, Sorting Levels and summary statics\n")

# doble indexacion en
df = pd.DataFrame({'num_legs': [4, 4, 2, 2],
                  'num_wings': [0, 0, 2, 2],
                   'class': ['mammal', 'mammal', 'mammal', 'bird'],
                   'animal': ['cat', 'dog', 'bat', 'penguin'],
                   'locomotion': ['walks', 'walks', 'flies', 'walks']})

df = df.set_index(['class', 'animal', 'locomotion'])
print(df)
print()

# intercambia la ubicacion de 2 niveles
print(df.swaplevel("class", "animal"))
print()
# con columnas no funciona
#print(df.swaplevel("num_legs", "num_wings"))
print()
# asi se puede hacer la modificacion de ubicacion sin el swaplevel de columnas
print(df[["num_wings", "num_legs"]])
print()

# para ordernar segun nivel de indexacion
print(df[["num_wings", "num_legs"]].sort_index(level=1))
print()

# summary statics
# se puede hacer sin hacer el group by pero va a ser eliminado en futuras versiones
print(df.groupby(level=0).sum())
