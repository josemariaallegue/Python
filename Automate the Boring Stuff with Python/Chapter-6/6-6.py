from typing import Text


print("String metodos - strip(), rstrip(), lstrip()")
texto = "   Hola mundo!   "
print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())
print("")

texto = "***Hola mundo!***"
print(texto)
print(texto.strip("*"))
print(texto.rstrip("*"))
print(texto.lstrip("*"))
