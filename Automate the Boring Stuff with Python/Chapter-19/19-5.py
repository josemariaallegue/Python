from random import randrange
from PIL import Image
from pathlib import Path

print("Changing Individual Pixels")
path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19")

newImage = Image.new("RGBA", (100, 100))

for i in range(100):
    for j in range(100):
        newImage.putpixel((i, j), (randrange(0, 200, 1),
                          randrange(0, 200, 1), randrange(0, 200, 1), 255))
        #print(newImage.getpixel((i, j)))

newImage.save(Path(path, "individualPixel.png"))
