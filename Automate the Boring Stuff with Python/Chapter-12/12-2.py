import requests
from pathlib import Path

print("Web scraping - Downloading Files from the Web with the requests Module")
path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-12")

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
res.raise_for_status()  # para chequear si todo salio bien
print(res.status_code == requests.codes.ok)  # para chequear si todo salio bien
print(len(res.text))
print(res.text[:250])

# escritura de la data en un archivo
file = open(Path(path, "Romeo and Juliet.txt"), "wb")  # escritura en binario
for chunk in res.iter_content(100000):
    file.write(chunk)

file.close()
