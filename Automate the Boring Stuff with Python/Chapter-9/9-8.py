from pathlib import Path

print("Reading and writing files - File Reading/Writing Process")

path = Path(
    "D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-9\9-8.txt")

# se puede hacer el manejo de archivos con Path pero conviene hacerlo con
# open(), read(), write() y cloe()
# .write_text si no existe el archivo lo crea y si exite lo pisa
path.write_text("Hola mundos!")
print(path.read_text())

# r para indicar que solo vamos a leer, w para escribir y si existe el archivo sobreescribir
# a para append
file = open(path, mode="r")
print(file.writable())  # me indica que el archivo no se puede escribir
print(file.read())

# no se pueden leer mas de una vez el archivo porque cambia el lugar del puntero del archivo
# hay que cambiar la ubicacion o cerar y volver a abrir antes de leer
print(file.readlines())
