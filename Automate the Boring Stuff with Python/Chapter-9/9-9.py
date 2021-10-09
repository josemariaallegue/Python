from pathlib import Path
import shelve
import os
from pathlib import Path

print("Reading and writing files - Saving Variables with the shelve Module")

# el path debe contener el archivo si no se guarda correctamente
path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-9", "shelve")
cats = ['Zophie', 'Pooka', 'Simon']

shelfFile = shelve.open(str(path))
shelfFile["cats"] = cats
shelfFile.close()

shelfFile = shelve.open(str(path))
print(type(shelfFile))
print(shelfFile["cats"])
print(shelfFile["cats"][1])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
