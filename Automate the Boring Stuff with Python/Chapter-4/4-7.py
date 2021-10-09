print("Referencias")
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)
"""When you assign 42 to the spam variable, you are actually creating the 42 value in the computer’s memory 
and storing a reference to it in the spam variable. When you copy the value in spam and assign it to the variable 
cheese, you are actually copying the reference. Both the spam and cheese variables refer to the 42 value in 
the computer’s memory. When you later change the value in spam to 100, you’re creating a new 100 value and storing 
a reference to it in spam. This doesn’t affect the value in cheese. Integers are immutable values that don’t 
change; changing the spam variable is actually making it refer to a completely different value in memory."""

"""But lists don’t work this way, because list values can change; that is, lists are mutable. Here is some code that 
will make this distinction easier to understand. Enter this into the interactive shell:"""
spam = [0, 1, 2, 3, 4, 5]
cheese = spam # The reference is being copied, not the list.
cheese[1] = 'Hello!' # This changes the list value.
print(spam)
print(cheese) # The cheese variable refers to the same list.
print("")

print("Id") # nos indica la ubicacion en memoria
print("inmutables - cambia el id al cambiar el valor")
print(id("hola mundo"))
print(id("hola mundo"))
print(id("hola mundo1"))
print("")

hola = "hola"
print(id(hola))
hola ="adios"
print(id(hola))
print("")

print("mutables - no cambia el id al cambaiar el valor")
lista  = [1,2,3]
lista2 = lista
print(id(lista))
lista.append(5)
print(id(lista))
print(id(lista2))