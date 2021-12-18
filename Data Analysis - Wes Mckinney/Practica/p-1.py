import pandas as pd
from pathlib import Path


ruta = Path(r"F:\Prueba")


columnas = ["COLUMNA" + str(x) for x in range(1, 12)]


df = pd.read_csv(Path(ruta, "C240000000002111.txt"), sep="\t",
                 encoding="ANSI", header=0, skiprows=1, names=columnas, skipfooter=1, engine="python")

