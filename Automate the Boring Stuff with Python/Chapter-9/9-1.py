from os import path
from pathlib import Path


print("Reading and writing files - introduction")

# como windows no usa el mismo formato de rutas que linux y mac conviene generar las rutas a travez de path
path = Path("carpeta1", "carpeta2", "archivo1")
print(path)
print(type(path))
print("")

# join method y concatenacion con /
path1 = Path("carpeta1", "carpeta2")
path2 = Path("carpetaA", "carpetaB", "archivoA")
# el joinpath es mas seguro porque el / no funcionaria en mac y linux
print(path1.joinpath(path2))
print(path1/path2)
