def collatz(number:int):

    if(number%2 == 0):
        print(str(number/2))
        return number/2
    else:
        print(str(3 * number + 1))
        return 3 * number + 1


print("Ingrese un numero entero mayor a 1")
try:
    number = int(input())

    while number != 1:
        number = collatz(number)

except:
    print("Error en el numero ingresado")