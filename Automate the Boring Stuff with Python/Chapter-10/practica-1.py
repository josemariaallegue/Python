import os
from pathlib import Path
import shutil

path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-10")
newPath = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-10\practica-1")

for folder, subFolders, files in os.walk(path):
    for file in Path(folder).glob("*.zip"):
        if(not Path(newPath, file.name).exists()):
            shutil.copy(file, newPath)
            print(f"Se copio {file.name}")
        else:
            print(f"No se copio {file.name}")
