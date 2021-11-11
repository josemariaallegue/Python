from os import path
from PIL import Image
from pathlib import Path

print("Resizing")
path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19")

catImage = Image.open(Path(path, "zophie.png"))
width, height = catImage.size
quaterSizeImage = catImage.resize((int(width/2), int(height/2)))
quaterSizeImage.save(Path(path, "quaterSize.png"))

print(catImage.size)
print(quaterSizeImage.size, "\n")

print("Rotating - Transpose/Mirror")
catImage.rotate(90).save(Path(path, "rotatedImage.png"))
catImage.rotate(90, expand=True).save(Path(path, "rotatedImageExpanded.png"))
catImage.transpose(Image.FLIP_LEFT_RIGHT).save(
    Path(path, "mirrorLeftRight.png"))
catImage.transpose(Image.FLIP_TOP_BOTTOM).save(
    Path(path, "mirrorTopBottom.png"))
