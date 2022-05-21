import pandas as pd
import numpy as np

print("Detecting and Filtering Outliers\n")

df = pd.DataFrame(np.random.randn(1000, 4))

print(df.head())
print()
print(df.describe())
print()
# filtro por todos los valores en columna 2 con
# valor absoluto mayor a 3
print(df[np.abs(df[2]) > 3])
print()
# para filtrar en todas las columnas hay que usar any
print(df[(np.abs(df) > 3).any(1)])
