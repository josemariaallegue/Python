import openpyxl
from pathlib import Path

print("Excel - creacion/eliminacion de elementos, escritura de datos y guardado")
path = Path(r"C:\Users\jmallegue\Documents\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-13")

wbNuevo = openpyxl.Workbook()  # creacion de libro
wbNuevo.create_sheet("Prueba", 0,)  # creacion de hoja
wbNuevo.remove(wbNuevo["Sheet"])  # eliminacion de hoja

wsHoja = wbNuevo["Prueba"]
wsHoja["A1"] = "Hola mundo"  # escritura de datos

wbNuevo.save(Path(path, "Ejemplo1.xlsx"))  # guardado de libro
