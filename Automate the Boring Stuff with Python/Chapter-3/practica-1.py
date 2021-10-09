from time import sleep

def modulo(espacios: int) -> str:
          
    sleep(0.1)

    return " " * espacios + "********"

while True:

    for i in range(0,30,1):
        print(modulo(i))
    for i in range(30,0,-1):
        print(modulo(i))


