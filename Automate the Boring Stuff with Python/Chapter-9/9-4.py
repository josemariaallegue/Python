from pathlib import Path
import os

print("Reading and writing files - creacion de directorios")

# con os
# si alguno de las carpetas no existe la crea
path = "C:\\delicious\\walnut\\waffles"
os.makedirs(path)
os.rmdir(path)

# con Path
# no puede crear multi capetas al mimo tiempo como os
Path(path).mkdir()
Path(path).unlink()
