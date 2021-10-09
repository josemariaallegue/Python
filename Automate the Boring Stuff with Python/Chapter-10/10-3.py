
from pathlib import Path
import zipfile

print("Organazing files - Compressing Files with the zipfile Module")

# creacion del objeto zipfile
path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-10\Zip")
zipAux = zipfile.ZipFile(Path(path, "Cats.zip"))

# listar los elementos de un zip
print(zipAux.namelist())

# obtener informacion de los elementos de un zip
catsInfo = zipAux.getinfo('Cats/cat1.txt')
print(str(catsInfo.file_size))
print(str(catsInfo.compress_size))
print(
    f'Compressed file is {round(catsInfo.file_size / catsInfo.compress_size, 2)}x smaller!')

# descomprimir el archivo
zipAux.extractall(path)

# descomprimir elementos del archivo
zipAux.extract('Cats/cat2.txt', path)

# creacion de zips
zipAux2 = zipfile.ZipFile(Path(path, "New.zip"), mode="w")
# el tema de esto es que tambien le pasa todas las carpetas anteriores
zipAux2.write(Path(path, "New.txt"), compress_type=zipfile.ZIP_DEFLATED)
