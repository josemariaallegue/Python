import pandas as pd
import numpy as np

print("Renaming Axis Indexes\n")
df = pd.DataFrame(np.arange(12).reshape((3, 4)),
                  index=['Ohio', 'Colorado', 'New York'],
                  columns=['one', 'two', 'three', 'four'])

# renombramiento de filas in place
df.index = df.index.map(lambda x: x.upper())
print(df.index)
print()

# renombramiento de columnas in place
df.columns = df.columns.map(lambda x: x.upper())
print(df.columns)
print()

# renombramiento de filas y columnas al mismo tiempo
df.rename(index={'OHIO': 'INDIANA'},
          columns={'three': 'peekaboo'},
          inplace=True)
print(df)
