import pandas as pd
from pathlib import Path

print("Reading Text Files in Pieces\n")

ruta = Path(
    r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Archivos\example3.csv")

df = pd.read_csv(ruta, sep=",", encoding="UTF8",
                 header=0, index_col="id", nrows=25)

print(df)
