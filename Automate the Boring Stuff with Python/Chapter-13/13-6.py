import openpyxl
from openpyxl.styles import Font
from pathlib import Path

print("Excel - formatos filas y columnas")
path = Path(
    r"C:\Users\jmallegue\Documents\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-13\Ejemplo1.xlsx")

wbExample = openpyxl.load_workbook(path)
wsSheet1 = wbExample["Prueba"]

wsSheet1['C1'] = 'Tall row'
wsSheet1['C2'] = 'Wide column'
# Set the height and width:
wsSheet1.row_dimensions[1].height = 70
wsSheet1.column_dimensions['C'].width = 20

wbExample.save(path)
