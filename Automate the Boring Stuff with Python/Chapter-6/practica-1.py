from typing import TextIO
import pyperclip
lista = pyperclip.paste().split("\n")

for i in range(len(lista)):
    lista[i] = "* " + str(lista[i])

texto = "\n".join(lista)

pyperclip.copy(texto)
print(pyperclip.paste())
