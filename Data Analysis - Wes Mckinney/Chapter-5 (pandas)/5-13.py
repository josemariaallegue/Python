import pandas as pd
import numpy as np

print("Arithmetic and Data Alignment\n")

"""When you are adding together objects, if any
index pairs are not the same, the respective index in the result will be the union of the
index pairs.
The internal data alignment introduces missing values in the label locations that don’t
overlap."""

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df1)
print()
print(df2)
print()

print(df1 + df2)  # en los index que no coinciden se pone Nan
print()

# con fill_value estableces un valor predterminado
print(df1.add(df2, fill_value=100))
print()

# fill_value tambien se puede aplicar cuando se reindexa
print(df1.reindex(columns=df2.columns, fill_value=0))
