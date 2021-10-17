import openpyxl
import pyinputplus as pyip
from pathlib import Path

path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-13", "Practica-2.xlsx")

# revision de existencia
if(path.exists()):
    wbAux = openpyxl.load_workbook(path)
    wsAux = wbAux["Sheet1"]

else:
    wbAux = openpyxl.Workbook()
    wsAux = wbAux("Sheet")
    wbAux.save(path)


desde = pyip.inputNum(
    "Ingrese desde que fila desea insertar filas en blanco: ", default=0)
cantidad = pyip.inputNum(
    "Ingrese cuantas filas en blanco desea ingresar: ", default=0)

wsAux.insert_rows(desde+1, cantidad)

wbAux.save(path)
