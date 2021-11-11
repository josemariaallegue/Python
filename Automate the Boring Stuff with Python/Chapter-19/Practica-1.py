from pathlib import Path
from PIL import Image

path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19")
waterMark = Image.open(Path(path, "catlogo.png"))
extensions = [".jpg", ".png"]

for extension in extensions:

    for file in path.glob(f"*{extension}"):

        auxImage = Image.open(file)
        widht, height = auxImage.size
        aspectRatio = widht/height

        if(widht > 300):
            rezise = 300/widht
            newHeight = int(height*rezise)
            auxImage.resize(300, newHeight)
            print(300/(height*rezise))
        elif(height > 300):
            rezise = 300/height
            auxImage.resize(int(widht*rezise), 300,)
            print((widht*rezise)/300)
