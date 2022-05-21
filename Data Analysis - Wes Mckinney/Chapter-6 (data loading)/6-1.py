import pandas as pd
from pathlib import Path

print("Reading and Writing Data in Text Format\n")

archivo = Path(
    r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Archivos\example1.csv")
archivo2 = Path(
    r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Archivos\example2.csv")

# read_csv por defecto tiene separador por "," pero igual se puede aclarar
# con sep=","
print(pd.read_csv(archivo, sep=","))
print()

# al poner header=none decimos que no hay encabezado
# y que creo uno
print(pd.read_csv(archivo, sep=",", header=None))
print()

# podemos establecer los nombres de las columnas que queramos
print(pd.read_csv(archivo, sep=",", names=[
      "columna1", "columna2", "columna3", "columna4", "columna5"]))
print()

# podemos establecer que una de las columnas sea el index
# podemos usar mas de una columna como index
print(pd.read_csv(archivo, sep=",", names=[
    "columna1", "columna2", "columna3", "columna4", "columna5"],
    index_col=["columna5", "columna4"]))
print()

# para saltar filas durante la importacion se usa skiprows
print(pd.read_csv(archivo, sep=",", skiprows=[1]))
print()

# manejando valores faltantes
print(pd.read_csv(archivo2, sep=","))
print()
print(pd.read_csv(archivo2, sep=",").isnull())
print()
# a na_values se la puede pasar un diccionario con los
# que hay que remplzar en cada columna
# na_value hace "Sequence of values to replace with NA"
print(pd.read_csv(archivo2, sep=",", na_values={
      'message': ['foo', 'NA'], 'something': ['two']}))
