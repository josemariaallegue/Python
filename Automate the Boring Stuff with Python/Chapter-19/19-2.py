from PIL import Image
from pathlib import Path

path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19\zophie.png")

# obtener una image como objeto imagen
catImage = Image.open(path)

# informacion general de la imagen
print(catImage.size)
print(catImage.filename)
print(catImage.format)
print(catImage.format_description)

# metodo para salvar una imagen
catImage.save(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19\zophie.jpg")

# creacion de una nueva imagen en blanclo
newImage = Image.new("RGBA", (100, 100), "PURPLE")
newImage.save(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19\purple.png")

newImage = Image.new("RGBA", (100, 100), (200, 20, 20, 20))
newImage.save(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19\mix.png")

# recorte de imagen
"""newCrop = Image.open(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19\zophie.png").crop((335, 345, 565, 560))"""
newCrop = catImage.crop((335, 345, 565, 560))
newCrop.save(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19\crop.jpg")

# copiar imagen y pegado de una image dentro de otra
copyImage = catImage.copy()
copyImage.paste(newCrop, (0, 0))
copyImage.paste(newCrop, (400, 500))
copyImage.save(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-19\copyImage.jpg")
