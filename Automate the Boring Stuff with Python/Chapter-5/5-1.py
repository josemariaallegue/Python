print("Diccionarios- metodos keys(), value(), items()")

spam = {'color': 'red', 'age': 42}
print(spam.values())
for i in spam.values():
     print(i)
print("")

print(spam.items())
for i in spam.items():
     print(i)
print("")

print(spam.keys())
for i in spam.keys():
     print(i)
print("")

for i, j in spam.items():
    print(i)
    print(j)