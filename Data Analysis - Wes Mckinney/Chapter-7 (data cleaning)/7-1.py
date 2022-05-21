from os import sep
import pandas as pd
from pathlib import Path

print("Filtering Out Missing Data\n")

ruta = Path(
    r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Archivos\example5.csv")

df = pd.read_csv(ruta, sep=",", encoding="UTF8",
                 header=0, index_col="id", nrows=10)

# formas de filtrar los null
print(df[df.notnull()])  # solo funciona con series
print(df.dropna())

print(df.dropna(how="all"))  # solo se borran las filas que son todas null

# A related way to filter out DataFrame rows tends to concern time series data. Suppose
# you want to keep only rows containing a certain number of observations
print(df.dropna(thresh=2))
