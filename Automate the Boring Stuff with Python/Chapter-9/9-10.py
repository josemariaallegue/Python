from pathlib import Path
import os
import pprint

print("Reading and writing files - Saving Variables with the pprint.pformat() Function")

cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
path = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-9", "myCats.py")

print(pprint.pformat(cats))

fileObj = open(path, 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

# para poder agarrar los datos del archivo hay que importar el modulo
"""print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])"""
