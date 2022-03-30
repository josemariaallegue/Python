print("Generators\n")

# un generator es una funcion que devuelve un objeto iterable
# tiene por lo menos un yield
# recuerda los valores de las variables cada vez que es llamado y devuelve el siguiente valor


def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2


for i in squares():
    print(i)

print()
# otro ejemplo


def my_gen():
    # hace algo
    yield 0

    # hace algo
    yield 1

    # hace algo
    yield 2


aux = my_gen()

# next(iterador) permite ejecutar la siguiente iteracion
print(next(aux))
print(next(aux))
print(next(aux))
# iterar una cuarta vez no es posible porque no esta codeado en la funcion
# print(next(aux))
print()


print("Generator expresssions\n")
# parecido a list, set and dict comprehensions
# creacion del generator en una linea siendo menos verboso
gen = (x ** 2 for x in range(10))

"""for i in gen:
    print(i)"""

print(next(gen))
print(next(gen))
print(next(gen))
