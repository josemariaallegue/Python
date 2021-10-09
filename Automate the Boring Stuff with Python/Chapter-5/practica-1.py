message = "It was a bright cold day in April, and the clocks were striking thirteen"

letras = {}
for character in message:
    letras.setdefault(character,0)
    letras[character] += 1

for items in letras.items():
    print(items)
