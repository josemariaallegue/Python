print("string metodos - startwith(), endwith()")
print('Hello, world!'.startswith('Hello'))
print('Hello, world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello, world!'.startswith('Hello, world!'))
print('Hello, world!'.endswith('Hello, world!'))
print("")

print("string metodos - join(), split(), partition()")
texto = "hola "
print(texto.join(["1", "2", "3"]))

texto = "Mi nombre es jose maria allegue"
print(texto.split())

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

print('Hello, world!'.partition('w'))
print("Hello, world!".partition('world'))
primera, segunda, tercera = "hello, world!".partition("w")
print(primera + segunda + tercera)
