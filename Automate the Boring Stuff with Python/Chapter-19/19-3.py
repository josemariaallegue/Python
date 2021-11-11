from os import path
from PIL import Image
from pathlib import Path

print("Create mosaic")
path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19")

catImage = Image.open(Path(path, "zophie.png"))
cropImage = Image.open(Path(path, "crop.png"))

widht, height = catImage.size
widhtCrop, heightCrop = cropImage.size

for i in range(0, widht, widhtCrop):
    for j in range(0, height, heightCrop):
        catImage.paste(cropImage, (i, j))


catImage.save(Path(path, "mosaic.png"))
