def funcion1():
    print(a)
    # declarcion de variable globar dentro de funcion
    # mala practica
    global b
    b = 2


def funcion2():
    # multiple retorno
    # lo que retorna en realidad es un tuple
    return 1, 2, 3, 4


# declaracion de variable goblal
a = 1

funcion1()
print(b)
numero1, numero2, numero3, numero4 = funcion2()
