import os
from pathlib import Path
import os
import send2trash

path1 = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-10\practica-1")

for folder, subFolders, files in os.walk(path1):

    for subFolder in subFolders:
        pathAux = Path(folder,  subFolder)
        if(os.path.getsize(str(pathAux)) > 100):
            # send2trash.send2trash(pathAux)
            print(
                f"El elemento {subFolder} pesa {os.path.getsize(str(pathAux))}")

    for file in files:
        pathAux = Path(folder,  file)
        if(os.path.getsize(str(pathAux)) > 100):
            # send2trash.send2trash(pathAux)
            print(
                f"El elemento {file} pesa {os.path.getsize(str(pathAux))}")
