from ast import Str
from pathlib import Path
import os
import re


path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-10\practica-3")
numeroAnterior = 0
reObject = re.compile("(\d)+")

# para crear los archivos
"""for i in range(1, 20):
    file = open(Path(path, "spam"+str(i)+".txt"), "x")"""


for file in sorted(path.glob(r"spam*.txt")):

    numeroActual = int(reObject.search(file.name).group())

    if((numeroActual - numeroAnterior) > 1):
        for i in range(numeroAnterior, numeroActual-1):

            file = open(
                Path(path, "spam"+str(i+1)+".txt"), "x")
            file.close()

    numeroAnterior = numeroActual
