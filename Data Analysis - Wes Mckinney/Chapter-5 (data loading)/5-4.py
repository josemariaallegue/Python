import pandas as pd
from pathlib import Path

print("JSON Data\n")

ruta = Path(
    r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Archivos\example4.json")

df = pd.read_json(ruta)

print(df)
