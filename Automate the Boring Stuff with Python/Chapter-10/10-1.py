import shutil
from pathlib import Path
import send2trash

print("Organazing files - shutil")
"""The shutil (or shell utilities) module has functions to let you copy, move, rename,
and delete files in your Python programs."""

path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-10\aux1")
path2 = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-10\aux2")

# se copia un solo archivo
# se puede cambiar el nombre del elemento unificando un nombre al final
shutil.copy(Path(path, "texto1.txt"), path2)

# se copia todo de una ruta a una ruta nueva
# si existe el folder de destino se genera error
if(not path2.is_dir()):
    print(shutil.copytree(path, path2))

# mover elementos
# se puede cambiar el nombre del elemento unificando un nombre al final
if(not Path(path2, "texto3.txt").is_file()):
    shutil.move(Path(path, "texto3.txt"), path2)
else:
    shutil.move(Path(path2, "texto3.txt"), path)

# eliminancion de elementos
# os.unlink(path) will delete the file at path.
# os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
# estos metodos eliminan directamete el archivo por esto conviene usar "send2trash

file = open(Path(path, "Delete.txt"), "x")
file.close()
send2trash.send2trash(Path(path, "Delete.txt"))
