import os
from pathlib import Path

print("Reading and writing files - parts of paths")

print("Elementos de un objeto Path")
path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Imagenes\9-3.jpg")
print(path.anchor)
print(path.drive)
print(path.name)
print(path.stem)
print(path.suffix)
print(str(path.parent))  # devuelve el primer elemento padre
print(str(path.parents[0]))  # devuelve el x elemento padre
print(str(path.parents[1]))
print(str(path.parents[2]))
print("")

# si se quiere un lista de los elementos de una ruta
print(str(path).split(os.sep))
