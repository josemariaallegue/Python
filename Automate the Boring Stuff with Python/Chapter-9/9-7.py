import os
from pathlib import Path

print("Reading and writing files - folder contents and Path Validity")

path = Path(r"D:\Imagenes\Wallpapers")

# exists() para chequear la existencia de la ruta
if(path.exists()):
    for file in os.listdir(path):
        #print(        f"Elemento: {file} - Tamaño {os.path.getsize(Path(path, file))/1000000}")
        break

    # If you want to work on specific files, the glob() method is simpler to use than listdir().
    # Path objects have a glob() method for listing the contents of a folder according to a glob pattern.
    for file in path.glob("*.png"):
        if(Path(path, file).is_file()):  # para chequear la existencia de la ruta y si es archivo
            print(
                f"Elemento: {file} - Tamaño {os.path.getsize(Path(path, file))/1000000}")

print(path.is_dir())  # para chequear la existencia de la ruta y si es folder
