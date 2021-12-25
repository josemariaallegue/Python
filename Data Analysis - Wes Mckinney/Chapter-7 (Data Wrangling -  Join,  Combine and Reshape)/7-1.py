import numpy as np
import pandas as pd

print("Hierarchical Indexing\n")

df = pd.DataFrame(np.random.randn(9),
                  index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                         [1, 2, 3, 1, 3, 1, 2, 2, 3]])

print(df)
print()
print(df.index)
print()
print(df.loc["b"])
print()
print(df.loc[:, 2])
print()
