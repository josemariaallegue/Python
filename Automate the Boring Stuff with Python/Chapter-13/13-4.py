import openpyxl
from openpyxl.styles import Font
from pathlib import Path

print("Excel - formato basico")
path = Path(
    r"C:\Users\jmallegue\Documents\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-13\Ejemplo1.xlsx")

wbExample = openpyxl.load_workbook(path)
wsSheet1 = wbExample["Prueba"]

font1 = Font(name="calibri", italic=True, bold=True, size=15)
font2 = Font(name="Arial", strikethrough=True, bold=True, size=25)

wsSheet1["A1"].font = font1
wsSheet1["A1"] = "Calibiri underline bold 15"
wsSheet1["A2"].font = font2
wsSheet1["A2"] = "Arial italics bold 25"

wbExample.save(path)
