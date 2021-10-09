import os
import shutil
from pathlib import Path
import os

print("Organazing files - Walking a Directory Tree")

# se utiliza os.walk() en un form
# devuelve tres elementos:
# A string of the current folder’s name
# A list of strings of the folders in the current folder
# A list of strings of the files in the current folder

path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-10")

for folder, subFolders, files in os.walk(path):
    print(f"Folder is: {str(folder)}")

    for subFolder in subFolders:
        print(f"Sub folder is: {str(subFolder)}")

    for file in files:
        print(f"File is: {str(file)}")
