print("Lambda\n")

# son funciones simples escritas de forma mas concisa


def apply_to_list(some_list, f):
    return [f(x) for x in some_list]


ints = [4, 0, 1, 5, 6]
# la primer x respresenta el parametro de la funcion
# la parte luego del : representa el retorno
print(apply_to_list(ints, lambda x: x * 2))
