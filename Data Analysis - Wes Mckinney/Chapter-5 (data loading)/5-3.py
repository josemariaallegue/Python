import pandas as pd
from pathlib import Path

print("Writing Data to Text Format\n")

ruta = Path(
    r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Archivos")

df = pd.read_csv(Path(ruta, "example3.csv"), sep=",", encoding="UTF8",
                 header=0, index_col="id", nrows=25)

df.to_csv(Path(ruta, "ejemplo guardado.csv"), sep=",",
          encoding="UTF8", header=True, index=True, na_rep="NULL",
          columns=["last_name", "gender"])
