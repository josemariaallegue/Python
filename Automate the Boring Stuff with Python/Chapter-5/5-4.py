import pprint

print("pprint library - para mostrar diccionarios")
message = "It was a bright cold day in April, and the clocks were striking thirteen"

letras = {}
for character in message:
    letras.setdefault(character,0)
    letras[character] += 1

pprint.pprint(letras)
print(pprint.pformat(letras)) # devuelve un string con el mismo formato que pprint.pprint()
