import openpyxl
from openpyxl.styles import Font
from pathlib import Path

print("Excel - formulas")
path = Path(
    r"C:\Users\jmallegue\Documents\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-13\Ejemplo1.xlsx")

wbExample = openpyxl.load_workbook(path)
wsSheet1 = wbExample["Prueba"]

wsSheet1["B1"] = 1
wsSheet1["B2"] = 2
wsSheet1["B3"] = "=SUM(B1:B2)"  # las formulas deben ser en ingles

wbExample.save(path)
