from os import sep
import pandas as pd
from pathlib import Path

print("Filling In Missing Data\n")

ruta = Path(
    r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Archivos\example5.csv")

df = pd.read_csv(ruta, sep=",", encoding="UTF8",
                 header=0, index_col="id", nrows=10)

# se rellenan los null con algun valor
print(df.fillna(0))
# si se pasa un diccionar se puede hacer una distincion por columna
print(df.fillna({"last_name":"Natalia Natalia", "gender": "indefinido"}))
# se puede determinar que se llene con algun valor ya establecido en la columna
print(df.fillna(method="ffill"))
