from pathlib import Path
import re
import pyinputplus as pyinp


path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-9")

patron = pyinp.inputStr("Ingrese un patron: ")
reObject = re.compile(patron)

for file in path.glob("*.txt"):

    fileAux = open(Path(path, file))
    mo = reObject.findall(fileAux.read())
    print(
        f"En el archivo {file.name} se encontraron {len(mo)} palabras \n{str(mo)}")
